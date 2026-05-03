# 🔬 ResearchMind: Multi-Agent AI Research System

A production-ready **multi-agent AI research assistant** that autonomously performs **web search, content extraction, report generation, and critique**, mimicking a human research workflow.

Built using **LangChain, OpenAI, Tavily, and Streamlit**, this system demonstrates modern **agentic AI orchestration** in a real-world application.

---

## 🚀 Features

* 🔍 **Search Agent**
  Retrieves relevant, up-to-date information using Tavily Search API

* 🌐 **Reader Agent**
  Scrapes and cleans web content for deeper understanding

* ✍️ **Writer Agent**
  Generates structured, high-quality research reports

* 🧐 **Critic Agent**
  Evaluates the report and provides constructive feedback

* ⚡ **Streamlit UI**
  Interactive interface to run the full research pipeline

---

## 🧠 Architecture

```
User Input
   ↓
Search Agent (Web Search)
   ↓
Reader Agent (Scraping)
   ↓
Writer Chain (Report Generation)
   ↓
Critic Chain (Evaluation)
```

This modular design enables **scalable multi-agent workflows** and clean separation of responsibilities.

---

## 🛠️ Tech Stack

* **LangChain** – Agent orchestration
* **OpenAI API** – LLM for reasoning & generation
* **Tavily API** – Real-time web search
* **BeautifulSoup** – Web scraping
* **Streamlit** – UI & deployment
* **Python** – Core implementation

---

## 📦 Project Structure

```
.
├── app.py              # Streamlit UI
├── agents.py           # Agent and LLM setup
├── tools.py            # Web search & scraping tools
├── pipeline.py         # Multi-agent orchestration logic
├── requirements.txt    # Dependencies
├── .env                # Environment variables (NOT committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Aurosampad/Multi-Agent-based-Research-system.git
cd Multi-Agent-based-Research-system
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

⚠️ **Important:**

* Do NOT commit `.env`
* Keep API keys secure

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📊 Example Workflow

1. Enter a research topic
2. System searches relevant sources
3. Extracts detailed content
4. Generates structured report
5. Critic evaluates the output

---

## 🚨 Common Issues

### ❌ API Key Errors

Ensure `.env` is properly configured and loaded.

---

### ❌ OpenAI Quota Error (429)

Check billing and usage:
https://platform.openai.com/usage

---

### ❌ GitHub Push Blocked

Ensure `.env` is excluded via `.gitignore`.

---

## 🔐 Security Best Practices

* Never commit API keys
* Use `.env` for local development
* Use environment variables in deployment

---

## 🚀 Future Improvements

* 🔁 Multi-URL scraping (parallel execution)
* ⚡ Async agents for faster performance
* 🧠 LangGraph-based orchestration
* 📦 Docker deployment
* 💾 Caching & memory integration

---

## 👨‍💻 Author

**Aurosampad Mohanty**
Machine Learning Engineer | AI Systems Developer

---

## ⭐ If you found this useful

Give the repo a ⭐ and feel free to contribute!

---
