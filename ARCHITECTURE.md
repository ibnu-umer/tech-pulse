# 🧱 TechPulse Architecture

> This document describes the internal structure, module interactions, and async workflow of **TechPulse** — the asynchronous tech intelligence aggregator.


## ⚙️ Overview

**TechPulse** is designed to fetch and aggregate data from multiple external APIs (News, Reddit, GitHub, etc.) **concurrently** using Python’s `asyncio` and `aiohttp`.

It follows a **modular and extensible architecture**, separating responsibilities into three main layers:
1. **API Layer** — Handles communication with external APIs.
2. **Core Logic Layer** — Orchestrates async fetching, processing, and reporting.
3. **Interface Layer** — CLI entry point (`main.py`) and user interaction.


## 🧩 System Design

```plaintext
┌───────────────────────────────┐
│           main.py             │
│       CLI Input + Async Run   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     core/fetcher.py           │
│  - Launches async tasks       │
│  - Manages concurrency        │
│  - Handles retries/timeouts   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│    core/processor.py          │
│    - Normalizes API data      │
│    - Merges by topic          │
│    - Cleans structures        │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     core/reporter.py          │
│     - Formats output          |
│     - Saves JSON report       │
│     - Pretty prints CLI       │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     output/report.json        │
│   - Final aggregated data     │
└───────────────────────────────┘
```


## 📦 Folder Structure
```plaintext
techpulse/
├── main.py
├── core/
│   ├── fetcher.py        # Manages concurrent API calls
│   ├── processor.py      # Cleans + merges responses
│   ├── reporter.py       # Formats console + JSON output
├── apis/
│   ├── news_api.py       # GNews / NewsAPI integration
│   ├── reddit_api.py     # Reddit public API integration
│   └── github_api.py     # GitHub trending repo fetcher
└── output/
    └── techpulse_report.json
```



## 🧠 Core Components

### **1. `main.py`**
- **CLI entry point.**
- Parses user input (`--topics`, `--limit`, etc.).
- Initializes the event loop and triggers `fetch_all()`.
- Coordinates the entire async workflow.


### **2. `core/fetcher.py`**
- Opens a single `aiohttp.ClientSession` for all async calls.
- Creates async tasks for each **topic × API** combination.
- Uses `asyncio.gather()` to run all requests concurrently.
- Implements:
  - **Timeouts** via `asyncio.wait_for()`
  - **Retries** for transient network failures
  - **Rate limiting** with `asyncio.Semaphore`


### **3. `core/processor.py`**
- Receives raw results from the fetcher.
- Normalizes all API outputs into a unified data structure:

```python
  {
    "source": "news",
    "topic": "AI",
    "title": "OpenAI launches GPT-6",
    "url": "https://newsapi.org/...",
    "popularity": 2300
  }
```
- Groups data by topic.
- Prepares clean objects for reporting and export.


### **4. `core/reporter.py`**
- Formats the processed data into:
- Readable console output
- Persistent JSON report (/output/techpulse_report.json)
- Responsible for all presentation logic.

### **5. `apis/`**
- Each API integration is isolated in its own module for easy maintenance and scalability.
- news_api.py — Fetches from GNews or NewsAPI.
- reddit_api.py — Queries Reddit’s public JSON endpoint.
- github_api.py — Fetches trending repositories from GitHub API.

**Each module follows a standard async pattern:**
```python
async def fetch_<source>(session, topic) -> dict:
    ...
    return normalized_data
```
