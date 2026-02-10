# 📝 CrewAI Article Generation Workflow

An intelligent multi-agent system that automates the entire article creation process using CrewAI. This project orchestrates four specialized AI agents to research, write, review, and publish high-quality articles on any given topic.

## 🌟 Features

- **🌐 Modern Web UI**: Beautiful, responsive interface with real-time progress tracking
- **💻 CLI Support**: Traditional command-line interface still available
- **🤖 Multi-Agent Collaboration**: Four specialized agents work together seamlessly
- **🔍 Automated Research**: Intelligent information gathering on any topic
- **✍️ Content Creation**: AI-powered article writing based on research
- **📋 Quality Review**: Automated editing for clarity, accuracy, and grammar
- **📤 Markdown Publishing**: Final articles saved as formatted `.md` files
- **⚡ Real-Time Updates**: Live progress tracking via Server-Sent Events
- **🎨 Glassmorphism Design**: Modern UI with smooth animations and gradients
- **📥 Download & Copy**: Easy article export and clipboard functionality
- **🔐 Secure Configuration**: Environment-based API key management

## 🤖 Agent Workflow

The system consists of four specialized agents:

1. **Researcher Agent** 🔍
   - Gathers comprehensive information on the given topic
   - Provides detailed summaries of findings
   - Expert at finding and synthesizing relevant information

2. **Creator Agent** ✍️
   - Transforms research into engaging articles
   - Creates well-structured, informative content
   - Skilled at turning data into compelling narratives

3. **Reviewer Agent** 📋
   - Reviews and edits articles for quality
   - Ensures accuracy, clarity, and proper grammar
   - Meticulous editor focused on excellence

4. **Publisher Agent** 📤
   - Saves the final article as a Markdown file
   - Handles file formatting and output
   - Ensures proper document structure

## 🛠️ Tech Stack

**Backend:**
- **Python 3.x**
- **CrewAI**: Multi-agent orchestration framework
- **Flask**: Web framework for the UI
- **OpenAI API**: Powers the AI agents
- **python-dotenv**: Environment variable management

**Frontend:**
- **HTML5/CSS3**: Modern semantic markup and styling
- **Vanilla JavaScript**: No framework dependencies
- **Server-Sent Events (SSE)**: Real-time progress updates
- **Marked.js**: Markdown rendering library

## ⚡ Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd articelgen
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Add your OpenAI API key to .env
echo OPENAI_API_KEY=your_key_here > .env

# Start the Web UI
python app.py
# Then open http://127.0.0.1:5000 in your browser

# OR use CLI
python main.py
```

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd articelgen
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## 💻 Usage

### Option 1: Web UI (Recommended)

1. **Start the web server**
   ```bash
   # Activate virtual environment
   .venv\Scripts\activate
   
   # Run the Flask app
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://127.0.0.1:5000`
   - You'll see a modern, intuitive interface

3. **Generate an article**
   - Enter your topic in the input field
   - Click "Generate Article"
   - Watch real-time progress as agents work:
     - 🔍 Researcher gathers information
     - ✍️ Creator writes the article
     - 📋 Reviewer edits and improves
     - 📤 Publisher finalizes
   
4. **Download or copy**
   - Preview the article with markdown formatting
   - Download as `.md` file
   - Copy to clipboard

### Option 2: Command Line Interface

1. **Run the CLI application**
   ```bash
   # Activate virtual environment
   .venv\Scripts\activate
   
   # Run the script
   python main.py
   ```

2. **Enter your topic**
   - When prompted, type the topic you want an article about
   - Example: "Artificial Intelligence in Healthcare"

3. **Wait for completion**
   - The agents will work sequentially
   - Progress updates will be shown in the terminal
   - The final article will be saved as `article.md`

## 📁 Project Structure

```
articelgen/
├── app.py                 # Flask web server (Web UI)
├── main.py                # Core logic + CLI interface
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── publisher_agent.py     # Custom publisher agent
├── run.py                 # Alternative entry point
├── templates/
│   └── index.html         # Web UI main page
├── static/
│   ├── css/
│   │   └── style.css      # UI styles
│   └── js/
│       └── app.js         # Frontend logic
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── article.md            # Generated article output
```

## 🔧 How It Works

1. **Initialization**: The system loads environment variables and creates all four agents
2. **Task Definition**: Tasks are created and assigned to their respective agents
3. **Crew Orchestration**: CrewAI manages the workflow of research, creation, and review
4. **Sequential Execution**: 
   - Researcher gathers information
   - Creator writes based on research
   - Reviewer edits and improves
5. **Publishing**: The final reviewed article is saved as a Markdown file

## 📝 Example Output

The generated `article.md` file will contain a well-structured, researched article on your chosen topic, complete with:
- Clear introduction
- Well-organized sections
- Factual, researched content
- Proper grammar and formatting
- Professional tone

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure
- The `.gitignore` file is configured to exclude sensitive files
- For production use, implement proper authentication and HTTPS

## 🔧 Troubleshooting

### Web UI Issues

**Server won't start:**
```bash
# Make sure you're using the virtual environment
.venv\Scripts\python.exe app.py

# Check if Flask is installed
.venv\Scripts\pip.exe list | Select-String "flask"
```

**"Module not found" errors:**
```bash
# Reinstall dependencies in virtual environment
.venv\Scripts\pip.exe install -r requirements.txt
```

**JSON parsing errors in browser console:**
- The server should auto-reload with debug mode
- If not, restart the Flask server manually
- Clear browser cache and refresh

**Article generation stuck:**
- Check your OpenAI API key in `.env` file
- Verify you have API credits available
- Check the terminal for error messages

### CLI Issues

**"No module named 'crewai'" error:**
```bash
# Use virtual environment Python
.venv\Scripts\python.exe main.py
```

**API errors:**
- Verify `OPENAI_API_KEY` in `.env` file
- Check API key has proper permissions
- Ensure you have available API credits

### General Issues

**Virtual environment not activating:**
```bash
# Recreate virtual environment
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\pip.exe install -r requirements.txt
```

**Port 5000 already in use:**
```python
# Edit app.py, change the port:
app.run(debug=True, threaded=True, port=5001)
```

## 🚀 Deployment

### Deploy to Render (Recommended)

This application is ready to deploy to Render with zero configuration:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com) and sign in
   - Click **"New +"** → **"Blueprint"**
   - Connect your repository
   - Render will auto-detect `render.yaml`
   - Add your `OPENAI_API_KEY` in environment variables
   - Click **"Apply"** to deploy

3. **Access your app:**
   - Your app will be live at: `https://your-service-name.onrender.com`
   - First request may take 30-60 seconds (free tier spins down)

**📖 For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**

### Other Platforms

- **Railway**: Similar to Render, supports long-running tasks
- **Fly.io**: Good alternative with free tier
- **Heroku**: Requires paid plan (no free tier)
- ❌ **Vercel**: Not recommended (serverless timeout limits)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available for educational and commercial use.

## 🙏 Acknowledgments

- Built with [CrewAI](https://www.crewai.com/)
- Powered by [OpenAI](https://openai.com/)

---

**Made with ❤️ using CrewAI**
