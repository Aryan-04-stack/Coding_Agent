#  AI Coding Agent

An AI-powered coding agent built using **Python** and **Google Gemini API**.

The goal of this project is to understand how AI agents work internally by building one from scratch.

## 🚀 Features

- 📂 Inspect files and directories.
- 📖 Read existing files.
- ✍️ Create and modify files.
- 🐍 Execute Python programs.
- 🧠 Decide which tools to use based on user instructions.
- 🔄 Use an agent loop to interact with Gemini and execute tools.

## ⚙️ How It Works

The agent follows a simple workflow:

1. The user provides a task in natural language.
2. Gemini decides which tool is needed.
3. Python executes the requested tool.
4. The result is sent back to Gemini.
5. The process continues until the task is completed.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Function Calling
- OS and File Handling

## 💻 Getting Started

**1. Clone the repository**

```bash
git clone THIS_REPO_URL
cd THIS_REPO_NAME
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate it (Windows)**

```bash
.venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install google-genai
```

**5. Set your Gemini API key**

Set your `GEMINI_API_KEY` environment variable before running the agent. Never commit your API key to GitHub.

**6. Run the agent**

```bash
python bot_v2.py "Build a simple Python calculator"
```

## 🚧 Current Status

This project is still under development.

Some features, particularly permission handling and error handling, need further improvements. I'm actively working on making the agent more reliable and efficient.

## 🔮 Future Improvements

- Improve permission and approval handling.
- Prevent unnecessary repeated tool calls.
- Improve error handling.
- Add better execution safety.
- Support more tools and programming languages.

---

**Built with Python, curiosity, and lots of debugging!** 
