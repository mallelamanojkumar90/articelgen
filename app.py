from flask import Flask, render_template, request, jsonify, Response, send_file
from main import generate_article
import threading
import uuid
import time
import io
import json
import mimetypes
from datetime import datetime

# Initialize mimetypes for static files
mimetypes.init()
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__)

# In-memory storage for task status
tasks = {}

class TaskStatus:
    def __init__(self, task_id, topic):
        self.task_id = task_id
        self.topic = topic
        self.status = 'pending'  # pending, running, completed, error
        self.progress = []
        self.article = None
        self.error = None
        self.created_at = datetime.now()
        self.completed_at = None

def progress_callback(task_id, agent, status):
    """Callback function to update task progress"""
    if task_id in tasks:
        tasks[task_id].progress.append({
            'agent': agent,
            'status': status,
            'timestamp': datetime.now().isoformat()
        })

def generate_article_background(task_id, topic):
    """Background thread function to generate article"""
    try:
        tasks[task_id].status = 'running'
        
        # Create a progress callback bound to this task
        def callback(agent, status):
            progress_callback(task_id, agent, status)
        
        # Generate the article
        result = generate_article(topic, progress_callback=callback)
        
        if result['status'] == 'success':
            tasks[task_id].status = 'completed'
            tasks[task_id].article = result['article']
        else:
            tasks[task_id].status = 'error'
            tasks[task_id].error = result.get('error', 'Unknown error')
        
        tasks[task_id].completed_at = datetime.now()
        
    except Exception as e:
        tasks[task_id].status = 'error'
        tasks[task_id].error = str(e)
        tasks[task_id].completed_at = datetime.now()

@app.route('/')
def index():
    """Serve the main UI page"""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    """Start article generation"""
    data = request.get_json()
    topic = data.get('topic', '').strip()
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    # Create a new task
    task_id = str(uuid.uuid4())
    tasks[task_id] = TaskStatus(task_id, topic)
    
    # Start background thread
    thread = threading.Thread(target=generate_article_background, args=(task_id, topic))
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'task_id': task_id,
        'status': 'started',
        'topic': topic
    })

@app.route('/api/status/<task_id>')
def status_stream(task_id):
    """Server-Sent Events endpoint for real-time progress"""
    def generate_events():
        if task_id not in tasks:
            error_data = json.dumps({'error': 'Task not found'})
            yield f"data: {error_data}\n\n"
            return
        
        task = tasks[task_id]
        last_progress_count = 0
        keepalive_counter = 0
        
        while True:
            # Send new progress updates
            if len(task.progress) > last_progress_count:
                for i in range(last_progress_count, len(task.progress)):
                    progress = task.progress[i]
                    progress_data = json.dumps({
                        'type': 'progress',
                        'agent': progress['agent'],
                        'status': progress['status'],
                        'timestamp': progress['timestamp']
                    })
                    yield f"data: {progress_data}\n\n"
                last_progress_count = len(task.progress)
                keepalive_counter = 0  # Reset keepalive counter on activity
            
            # Send status update
            if task.status == 'completed':
                completed_data = json.dumps({
                    'type': 'completed',
                    'article': task.article
                })
                yield f"data: {completed_data}\n\n"
                break
            elif task.status == 'error':
                error_data = json.dumps({
                    'type': 'error',
                    'error': task.error
                })
                yield f"data: {error_data}\n\n"
                break
            
            # Send keepalive ping every 10 seconds (20 iterations * 0.5s)
            keepalive_counter += 1
            if keepalive_counter >= 20:
                yield ": keepalive\n\n"
                keepalive_counter = 0
            
            time.sleep(0.5)  # Poll every 500ms
    
    response = Response(generate_events(), mimetype='text/event-stream')
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['X-Accel-Buffering'] = 'no'
    response.headers['Connection'] = 'keep-alive'
    return response


@app.route('/api/download/<task_id>')
def download(task_id):
    """Download the generated article"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    task = tasks[task_id]
    
    if task.status != 'completed':
        return jsonify({'error': 'Article not ready'}), 400
    
    # Create a file-like object
    article_bytes = task.article.encode('utf-8')
    article_io = io.BytesIO(article_bytes)
    
    # Generate filename
    filename = f"article_{task.topic.replace(' ', '_')[:30]}.md"
    
    return send_file(
        article_io,
        mimetype='text/markdown',
        as_attachment=True,
        download_name=filename
    )

@app.route('/api/task/<task_id>')
def get_task(task_id):
    """Get task information"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    task = tasks[task_id]
    
    return jsonify({
        'task_id': task.task_id,
        'topic': task.topic,
        'status': task.status,
        'progress_count': len(task.progress),
        'created_at': task.created_at.isoformat(),
        'completed_at': task.completed_at.isoformat() if task.completed_at else None,
        'has_article': task.article is not None
    })

if __name__ == '__main__':
    import os
    
    # Check if running in production (Render sets PORT environment variable)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    if debug:
        print("🚀 Starting CrewAI Article Generator Web UI")
        print(f"📍 Open your browser to: http://127.0.0.1:{port}")
        print("Press Ctrl+C to stop the server\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)

