# 📝 CrewAI Article Generation Workflow

An intelligent multi-agent system that automates the entire article creation process using CrewAI. This project orchestrates four specialized AI agents to research, write, review, and publish high-quality articles on any given topic.

## 🌟 Features

- **Multi-Agent Collaboration**: Four specialized agents work together seamlessly
- **Automated Research**: Intelligent information gathering on any topic
- **Content Creation**: AI-powered article writing based on research
- **Quality Review**: Automated editing for clarity, accuracy, and grammar
- **Markdown Publishing**: Final articles saved as formatted `.md` files
- **Interactive CLI**: Simple command-line interface for topic input
- **Environment-based Configuration**: Secure API key management

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

- **Python 3.x**
- **CrewAI**: Multi-agent orchestration framework
- **OpenAI API**: Powers the AI agents
- **python-dotenv**: Environment variable management

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

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Enter your topic**
   - When prompted, type the topic you want an article about
   - Example: "Artificial Intelligence in Healthcare"

3. **Wait for the workflow to complete**
   - The agents will work sequentially:
     - Research the topic
     - Create an article
     - Review and edit
     - Publish to `article.md`

4. **Find your article**
   - The final article will be saved as `article.md` in the project directory

## 📁 Project Structure

```
articelgen/
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── main.py                # Main orchestration script
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── publisher_agent.py     # Custom publisher agent
├── run.py                 # Alternative entry point
└── article.md             # Generated article output
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
