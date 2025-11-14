from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from pydantic import BaseModel
from typing import List, Dict
from dotenv import load_dotenv
import os

from src.pr_review_agent.reviewer import AIReviewer
from src.pr_review_agent.services.github_service import get_pr_details

# Load environment
load_dotenv()

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize FastAPI
app = FastAPI(
    title="PR Review Agent - Multi-Agent System",
    description="AI-powered GitHub PR reviewer using Groq Llama 3.3",
    version="2.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Models
class PRRequest(BaseModel):
    repo: str
    pr_number: int

class AgentReview(BaseModel):
    agent_name: str
    agent_role: str
    findings: str
    issues_found: int

class FileReview(BaseModel):
    file: str
    additions: int
    deletions: int
    agents: List[AgentReview]

class PRReviewResponse(BaseModel):
    status: str
    pr_title: str
    pr_url: str
    pr_author: str
    files_reviewed: int
    reviews: List[FileReview]

# Endpoints
@app.get("/", include_in_schema=False)
async def redirect_to_ui():
    """Redirect root to UI"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/ui")

@app.get("/ui", response_class=HTMLResponse)
async def web_ui(request: Request):
    """Web UI for PR reviews"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    groq = bool(os.getenv("GROQ_API_KEY"))
    github = bool(os.getenv("GITHUB_TOKEN"))
    
    return {
        "status": "healthy" if (groq and github) else "configuration_error",
        "architecture": "multi-agent",
        "agents": [
            {
                "name": "Logic & Bug Analyzer",
                "role": "Identify logic errors, bugs, and edge cases",
                "status": "active" if groq else "not_configured"
            },
            {
                "name": "Security Auditor",
                "role": "Detect security vulnerabilities and risks",
                "status": "active" if groq else "not_configured"
            },
            {
                "name": "Performance Engineer",
                "role": "Find performance bottlenecks and inefficiencies",
                "status": "active" if groq else "not_configured"
            },
            {
                "name": "Code Quality Reviewer",
                "role": "Ensure maintainability and best practices",
                "status": "active" if groq else "not_configured"
            }
        ],
        "orchestration": "Sequential Multi-Agent Process",
        "llm": {
            "provider": "Groq",
            "model": "llama-3.3-70b-versatile",
            "configured": groq
        },
        "integrations": {
            "github": github,
            "groq": groq
        }
    }

@app.post("/review", response_model=PRReviewResponse)
def review_pr(request: PRRequest):
    """Review a GitHub Pull Request using multi-agent AI system"""
    try:
        print(f"\n{'='*70}")
        print(f"🔍 Starting Multi-Agent Review")
        print(f"{'='*70}")
        print(f"Repository: {request.repo}")
        print(f"PR Number: #{request.pr_number}")
        print(f"{'='*70}\n")
        
        pr_data = get_pr_details(request.repo, request.pr_number)
        
        if not pr_data["files"]:
            raise HTTPException(400, "No files with changes found in this PR")
        
        print(f"✅ Found {len(pr_data['files'])} file(s) with changes")
        print(f"📋 PR Title: {pr_data['title']}")
        print(f"👤 Author: {pr_data['author']}\n")
        
        reviewer = AIReviewer()
        reviews = []
        files_to_review = pr_data["files"][:3]
        
        for i, file in enumerate(files_to_review, 1):
            print(f"{'─'*70}")
            print(f"[{i}/{len(files_to_review)}] File: {file['filename']}")
            print(f"     Changes: +{file['additions']} -{file['deletions']}")
            print(f"{'─'*70}")
            
            agent_reviews = reviewer.review_code(file["filename"], file["patch"])
            
            reviews.append(FileReview(
                file=file["filename"],
                additions=file["additions"],
                deletions=file["deletions"],
                agents=agent_reviews
            ))
            
            print(f"✅ Review complete for {file['filename']}\n")
        
        print(f"{'='*70}")
        print(f"✨ Multi-Agent Review Finished Successfully!")
        print(f"{'='*70}\n")
        
        return PRReviewResponse(
            status="completed",
            pr_title=pr_data["title"],
            pr_url=pr_data["url"],
            pr_author=pr_data["author"],
            files_reviewed=len(reviews),
            reviews=reviews
        )
    
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"{'='*70}")
        print(f"❌ Error during review: {str(e)}")
        print(f"{'='*70}\n")
        raise HTTPException(500, f"Review failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
