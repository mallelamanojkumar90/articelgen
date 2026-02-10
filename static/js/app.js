// State management
let currentTaskId = null;
let eventSource = null;

// DOM elements
const articleForm = document.getElementById('articleForm');
const topicInput = document.getElementById('topicInput');
const generateBtn = document.getElementById('generateBtn');
const progressSection = document.getElementById('progressSection');
const articleSection = document.getElementById('articleSection');
const errorSection = document.getElementById('errorSection');
const agentIcon = document.getElementById('agentIcon');
const agentName = document.getElementById('agentName');
const agentStatus = document.getElementById('agentStatus');
const progressBar = document.getElementById('progressBar');
const logEntries = document.getElementById('logEntries');
const articlePreview = document.getElementById('articlePreview');
const errorMessage = document.getElementById('errorMessage');
const downloadBtn = document.getElementById('downloadBtn');
const copyBtn = document.getElementById('copyBtn');
const retryBtn = document.getElementById('retryBtn');

// Agent icons mapping
const agentIcons = {
    'Initializing': '⚙️',
    'Researcher': '🔍',
    'Creator': '✍️',
    'Reviewer': '📋',
    'Publisher': '📤',
    'Completed': '✅',
    'Error': '❌'
};

// Form submission
articleForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const topic = topicInput.value.trim();
    if (!topic) return;
    
    // Reset UI
    hideAllSections();
    progressSection.style.display = 'block';
    logEntries.innerHTML = '';
    progressBar.style.width = '0%';
    
    // Disable input
    generateBtn.disabled = true;
    topicInput.disabled = true;
    
    try {
        // Start generation
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topic })
        });
        
        if (!response.ok) {
            throw new Error('Failed to start generation');
        }
        
        const data = await response.json();
        currentTaskId = data.task_id;
        
        // Connect to SSE for progress updates
        connectToProgressStream(currentTaskId);
        
    } catch (error) {
        showError(error.message);
        resetForm();
    }
});

// Connect to Server-Sent Events stream
function connectToProgressStream(taskId) {
    if (eventSource) {
        eventSource.close();
    }
    
    eventSource = new EventSource(`/api/status/${taskId}`);
    
    eventSource.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            
            if (data.type === 'progress') {
                updateProgress(data.agent, data.status, data.timestamp);
            } else if (data.type === 'completed') {
                handleCompletion(data.article);
            } else if (data.type === 'error') {
                handleError(data.error);
            }
        } catch (error) {
            console.error('Error parsing SSE data:', error);
        }
    };
    
    eventSource.onerror = (error) => {
        console.error('SSE error:', error);
        eventSource.close();
    };
}

// Update progress UI
function updateProgress(agent, status, timestamp) {
    // Update current agent display
    agentIcon.textContent = agentIcons[agent] || '🤖';
    agentName.textContent = agent;
    agentStatus.textContent = status;
    
    // Update progress bar
    const progressMap = {
        'Initializing': 10,
        'Researcher': 30,
        'Creator': 60,
        'Reviewer': 85,
        'Publisher': 95,
        'Completed': 100
    };
    progressBar.style.width = `${progressMap[agent] || 0}%`;
    
    // Add log entry
    addLogEntry(agent, status, timestamp);
}

// Add entry to activity log
function addLogEntry(agent, status, timestamp) {
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    
    const time = new Date(timestamp).toLocaleTimeString();
    
    entry.innerHTML = `
        <div><strong>${agentIcons[agent] || '🤖'} ${agent}</strong></div>
        <div>${status}</div>
        <div class="timestamp">${time}</div>
    `;
    
    logEntries.appendChild(entry);
    logEntries.scrollTop = logEntries.scrollHeight;
}

// Handle successful completion
function handleCompletion(article) {
    if (eventSource) {
        eventSource.close();
    }
    
    // Hide progress, show article
    progressSection.style.display = 'none';
    articleSection.style.display = 'block';
    
    // Render markdown
    articlePreview.innerHTML = marked.parse(article);
    
    // Reset form
    resetForm();
}

// Handle error
function handleError(error) {
    if (eventSource) {
        eventSource.close();
    }
    
    showError(error);
    resetForm();
}

// Show error section
function showError(message) {
    hideAllSections();
    errorSection.style.display = 'block';
    errorMessage.textContent = message;
}

// Hide all sections
function hideAllSections() {
    progressSection.style.display = 'none';
    articleSection.style.display = 'none';
    errorSection.style.display = 'none';
}

// Reset form
function resetForm() {
    generateBtn.disabled = false;
    topicInput.disabled = false;
}

// Download article
downloadBtn.addEventListener('click', async () => {
    if (!currentTaskId) return;
    
    try {
        const response = await fetch(`/api/download/${currentTaskId}`);
        
        if (!response.ok) {
            throw new Error('Download failed');
        }
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `article_${Date.now()}.md`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
    } catch (error) {
        alert('Failed to download article: ' + error.message);
    }
});

// Copy article to clipboard
copyBtn.addEventListener('click', async () => {
    const articleText = articlePreview.textContent;
    
    try {
        await navigator.clipboard.writeText(articleText);
        
        // Visual feedback
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<span>✅</span> Copied!';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
        
    } catch (error) {
        alert('Failed to copy to clipboard');
    }
});

// Retry button
retryBtn.addEventListener('click', () => {
    hideAllSections();
    topicInput.focus();
});

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (eventSource) {
        eventSource.close();
    }
});
