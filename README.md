# 🤖 PR Review Agent

> AI-powered multi-agent code review system using Groq Llama 3.3 70B and parallel processing

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=render)](https://pr-review-agent-9tkx.onrender.com/ui)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-00a393?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3-FF6550?style=for-the-badge)](https://groq.com/)
[![Uptime](https://img.shields.io/badge/Uptime-99.9%25-success?style=for-the-badge)](https://stats.uptimerobot.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

## 🌐 Live Demo

**🚀 Try it now:** [https://pr-review-agent-9tkx.onrender.com/ui](https://pr-review-agent-9tkx.onrender.com/ui)


---

## 📖 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [API Documentation](#api-documentation)
- [Performance](#performance)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

PR Review Agent is an intelligent, production-ready code review system that leverages **4 specialized AI agents running in parallel** to provide comprehensive analysis of GitHub Pull Requests. Built for the **Lyzr Agent API Hackathon**, this system demonstrates advanced multi-agent orchestration using Groq's ultra-fast Llama 3.3 70B model.

### 💡 The Problem

Manual code reviews are:
- ⏰ **Time-consuming** - Hours spent reviewing each PR
- 🔍 **Inconsistent** - Different reviewers, different standards
- 🐛 **Error-prone** - Critical issues often missed
- 📊 **Single-perspective** - Limited to reviewer's expertise

### ✨ Our Solution

Automated multi-agent AI system that:
- ⚡ **4x Faster** - Parallel processing reduces review time to 10-15 seconds
- 🎯 **Comprehensive** - 4 specialized agents cover all aspects
- 🔒 **Consistent** - Same high-quality analysis every time
- 📈 **Multi-dimensional** - Logic, security, performance, and quality in one review

---

## 🔥 Key Features

### 🤖 Multi-Agent Architecture

Our system employs 4 specialized AI agents, each an expert in their domain:

| Agent | Focus Area | Key Responsibilities |
|-------|-----------|---------------------|
| **Logic & Bug Analyzer** | Correctness | Logic errors, edge cases, runtime issues, incorrect implementations |
| **Security Auditor** | Security | Vulnerabilities, injection risks, authentication flaws, data exposure |
| **Performance Engineer** | Efficiency | Bottlenecks, inefficient algorithms, memory leaks, optimization opportunities |
| **Code Quality Reviewer** | Maintainability | Best practices, naming conventions, code smells, documentation |

### ⚡ Parallel Processing

- **4x Speed Boost** - All agents run simultaneously using Python's ThreadPoolExecutor
- **10-15 Second Reviews** - Lightning-fast analysis without compromising quality
- **Scalable Architecture** - Easily add more agents or scale horizontally

### 🎨 Beautiful User Interface

- **Responsive Design** - Modern gradient UI that works on all devices
- **Real-time Updates** - Loading animations and progress tracking
- **Pre-configured Examples** - Test with Django, Node.js, and React PRs instantly

### 🔌 Seamless GitHub Integration

- **REST API Integration** - Direct connection to GitHub's API
- **Rich PR Data** - Fetches titles, diffs, file changes, and metadata
- **Public Repository Support** - Works with any public GitHub repo

---

## 🏗️ Architecture

## 🏗️ Architecture

| Step | Component                  | Description                                          |
|------|---------------------------|------------------------------------------------------|
| 1    | User Request               | Repository + PR Number submitted by user             |
| 2    | FastAPI Backend            | Receives request and handles API endpoints           |
| 3    | GitHub API Service         | Fetches PR details, file diffs, and metadata         |
| 4    | Agent Execution            | Runs 4 agents in parallel threads                   |
| 5    | Logic & Bug Analyzer       | Detects code bugs and logic errors                   |
| 6    | Security Auditor           | Finds security vulnerabilities                       |
| 7    | Performance Engineer       | Identifies bottlenecks and inefficiencies            |
| 8    | Code Quality Reviewer      | Checks for best practices and maintainability        |
| 9    | Groq Llama 3.3 70B (LLM)   | Ultra-fast inference for all agent analyses          |
| 10   | Structured Results (JSON)  | Aggregates agent findings into a single JSON result  |
| 11   | Web UI                     | Displays all findings to the user in a clean web view|



### Design Principles

- **🎯 Separation of Concerns** - Each agent focuses on a specific domain
- **⚡ Parallel Processing** - ThreadPoolExecutor for concurrent execution
- **🔄 RESTful API** - Clean, stateless HTTP endpoints
- **💚 Health Monitoring** - `/health` endpoint for uptime tracking
- **📊 Structured Output** - JSON responses for easy integration

---

## 🛠️ Tech Stack

### Backend Technologies

| Technology | Version | Purpose | Why We Chose It |
|------------|---------|---------|-----------------|
| **FastAPI** | 0.121+ | Web framework | High performance, automatic API docs, async support |
| **LangChain** | 1.0+ | LLM orchestration | Simplified prompt management, chaining capabilities |
| **Groq** | 0.34+ | LLM inference | Ultra-fast inference (up to 500 tokens/sec) |
| **PyGithub** | 2.8+ | GitHub API | Official Python wrapper for GitHub REST API |
| **Pydantic** | 2.12+ | Data validation | Type safety, automatic validation, serialization |
| **Python-dotenv** | 1.2+ | Environment management | Secure API key handling |

### Frontend Technologies

| Technology | Purpose |
|------------|---------|
| **HTML5/CSS3** | Structure and styling |
| **JavaScript (ES6+)** | Interactivity and async requests |
| **Jinja2** | Server-side templating |
| **Fetch API** | HTTP requests to backend |

### Infrastructure

| Service | Purpose | Tier |
|---------|---------|------|
| **Render** | Cloud hosting | Free (with auto-deploy) |
| **GitHub Actions** | CI/CD (optional) | Free |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Groq API Key ([Get one free](https://console.groq.com))
- GitHub Personal Access Token ([Create one](https://github.com/settings/tokens))

### Installation

1. Clone the repository
git clone https://github.com/Ashish7105/PR_REVIEW_AGENT.git
cd PR_REVIEW_AGENT

2. Create and activate virtual environment
python -m venv .venv

Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

text

### Environment Setup

Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key_here
GITHUB_TOKEN=your_github_token_here

text

### Run Locally

Start the development server
uvicorn api:app --reload --port 8000

Open your browser
Navigate to: http://localhost:8000/ui

---

## 💻 Usage Examples

### Web Interface

1. **Visit** the live demo or local URL
2. **Choose** a pre-configured example:
   - 🌐 **Django Framework** - `django/django` PR #1
   - 🟢 **Node.js Security** - `nodejs/node` PR #1
   - ⚛️ **React Testing** - `facebook/react` PR #1
3. **Or enter custom:**
   - Repository: `owner/repo` (e.g., `microsoft/vscode`)
   - PR Number: Numeric ID (e.g., `42`)
4. **Click** "🚀 Start Review"
5. **Wait** 10-30 seconds for comprehensive analysis
6. **View** detailed findings from all 4 agents

### API Usage

#### Health Check

curl https://pr-review-agent-9tkx.onrender.com/health


**Response:**
{
"status": "healthy",
"architecture": "multi-agent",
"agents": [
{
"name": "Logic & Bug Analyzer",
"status": "active"
},
...
],
"llm": {
"provider": "Groq",
"model": "llama-3.3-70b-versatile",
"configured": true
}
}

text

#### Submit PR for Review

curl -X POST https://pr-review-agent-9tkx.onrender.com/review
-H "Content-Type: application/json"
-d '{"repo": "django/django", "pr_number": 1}'

text

**Response:**
{
"status": "completed",
"pr_title": "Fix security issue in authentication",
"pr_author": "contributor",
"files_reviewed": 3,
"reviews": [
{
"file": "auth.py",
"additions": 10,
"deletions": 5,
"agents": [
{
"agent_name": "Logic & Bug Analyzer",
"findings": "...",
"issues_found": 2
},
...
]
}
]
}


---

## 📚 API Documentation

Once running, visit these endpoints:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Redirects to `/ui` |
| `GET` | `/ui` | Web interface |
| `GET` | `/health` | Health check status |
| `POST` | `/review` | Submit PR for review |

---

## ⚡ Performance

### Benchmarks

| Metric | Sequential | Parallel | Improvement |
|--------|-----------|----------|-------------|
| **Single File** | 40 sec | 10 sec | **4x faster** ⚡ |
| **3 Files** | 120 sec | 30 sec | **4x faster** ⚡ |
| **Response Time** | - | 300ms avg | Excellent ✅ |
| **Uptime** | - | 99.9% | Production-ready ✅ |

### Response Times

- **Minimum:** 251ms
- **Average:** 300ms
- **Maximum:** 398ms

---

## 🌍 Deployment

### Deploy to Render (Recommended)

1. **Fork** this repository
2. **Sign up** on [Render](https://render.com)
3. **Create** new Web Service
4. **Connect** your GitHub repository
5. **Configure** environment variables:
   - `GROQ_API_KEY`
   - `GITHUB_TOKEN`
     
6. **Deploy!** Render handles the rest

**Build Command:** `pip install -r requirements.txt`  
**Start Command:** `uvicorn api:app --host 0.0.0.0 --port $PORT`

### Docker (Coming Soon)

docker build -t pr-review-agent .
docker run -p 8000:8000 --env-file .env pr-review-agent





## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ashish Kumar**

- 🌐 GitHub: [@Ashish7105](https://github.com/Ashish7105)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/ashish-kumar-codes/)
- 📧 Email: ashishkum7105@gmail.com

---

## 🙏 Acknowledgments

- **Lyzr AI** - For hosting the Agent API Hackathon
- **Groq** - For providing ultra-fast LLM inference
- **LangChain** - For excellent LLM orchestration tools
- **Render** - For reliable cloud hosting
- **UptimeRobot** - For 24/7 monitoring

---

## 🎯 Built For


Showcasing the power of multi-agent AI systems for automated code review and quality assurance in software development workflows.

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Made with ❤️ by Ashish Kumar

[Live Demo](https://pr-review-agent-9tkx.onrender.com/ui) • [Report Bug](https://github.com/Ashish7105/PR_REVIEW_AGENT/issues) • [Request Feature](https://github.com/Ashish7105/PR_REVIEW_AGENT/issues)

</div>





