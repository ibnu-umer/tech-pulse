# ⚡ TechPulse — Async Tech Intelligence Aggregator

> A fast, asynchronous Python tool that aggregates **real-time tech news, Reddit discussions, and GitHub trends** for your chosen topics — all in one place.


## 🧠 Overview

TechPulse solves a simple but painful problem:
Tech professionals waste time jumping across News sites, Reddit, and GitHub to figure out what’s trending.
TechPulse automates that — fetching, filtering, and summarizing everything **concurrently** using `asyncio` and `aiohttp`.

You give it a few topics, it gives you a **real-time tech pulse report**.


## 🚀 Example Usage

```bash
python main.py --topics "AI, Python, Tesla" --limit 5
```

## 🚀 Example Output
**📊 TechPulse Report**

🔹 AI
  - 📰 OpenAI launches GPT-6 — https://newsapi.org/...
  - 💬 Reddit: "Prompt Engineering is Dead" — 2.3k upvotes
  - 💻 GitHub: huggingface/transformers — 125k ⭐

🔹 Python
  - 📰 Python 3.13 Released — https://gnews.io/...
  - 💻 GitHub: fastapi/fastapi — 75k ⭐


## 🧩 Features
  - 🔄 Async fetching from multiple APIs in parallel
  - 📰 Aggregates data from NewsAPI, Reddit, GitHub
  - ⚙️ Configurable topics and limits via CLI
  - 💾 Exports results as structured JSON
  - 🧠 Easily extendable (add more sources or processing layers)


## ⚙️ Tech Stack

| Component | Purpose |
|------------|----------|
| `asyncio` | Core async orchestration |
| `aiohttp` | Non-blocking HTTP client |
| `requests` | For any blocking fallback APIs |
| `argparse` | CLI argument handling |
| `json`, `pathlib` | Data formatting & output |


## 🧱 Project Structure

```plaintext
techpulse/
├── main.py
├── core/
│   ├── fetcher.py        # Manages concurrent API calls
│   ├── processor.py      # Cleans + merges responses
│   ├── reporter.py       # Formats console + JSON output
├── apis/
│   ├── news_api.py
│   ├── reddit_api.py
│   └── github_api.py
└── output/
    └── techpulse_report.json
```


## 🔑 Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/techpulse.git
cd techpulse
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Keys
Create a .env file and set:
```bash
NEWS_API_KEY=your_api_key_here
GITHUB_TOKEN=optional_token_here
(Reddit uses public endpoints; no auth needed for now.)
```

### 4. Run it
```bash
python main.py --topics "AI, Tesla"
```


## 📦 Output
- Console summary (pretty printed)
- JSON report at /output/techpulse_report.json


## 🧭 Roadmap
 - Add YouTube API integration
 - Add Hacker News scraper
 - Add async caching layer
 - Add sentiment analysis on Reddit discussions
 - Add Slack/email notifications


## 🧠 Author
TechPulse — built for developers who want the world’s tech chatter at a glance.
