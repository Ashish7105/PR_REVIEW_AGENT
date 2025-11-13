from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from dotenv import load_dotenv
import os

from src.pr_review_agent.reviewer import AIReviewer
from src.pr_review_agent.services.github_service import get_pr_details

# Load environment
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="PR Review Agent",
    description="AI-powered GitHub PR reviewer using Groq",
    version="1.0.0"
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
    repo: str  # Format: "owner/repo"
    pr_number: int

class ReviewResult(BaseModel):
    file: str
    additions: int
    deletions: int
    review: str

class PRReviewResponse(BaseModel):
    status: str
    pr_title: str
    pr_url: str
    pr_author: str
    files_reviewed: int
    reviews: List[ReviewResult]

# Endpoints
@app.get("/")
def root():
    return {
        "name": "PR Review Agent",
        "version": "1.0.0",
        "description": "AI code review powered by Groq Llama 3.1",
        "endpoints": ["/health", "/review"]
    }

@app.get("/health")
def health():
    groq = bool(os.getenv("GROQ_API_KEY"))
    github = bool(os.getenv("GITHUB_TOKEN"))
    
    return {
        "status": "healthy" if (groq and github) else "configuration_error",
        "llm": "groq/llama-3.1-70b-versatile",
        "groq_configured": groq,
        "github_configured": github
    }

@app.post("/review", response_model=PRReviewResponse)
def review_pr(request: PRRequest):
    """Review a GitHub Pull Request"""
    try:
        print(f"\n{'='*70}")
        print(f"🔍 Reviewing PR #{request.pr_number} from {request.repo}")
        print(f"{'='*70}\n")
        
        # Fetch PR data
        pr_data = get_pr_details(request.repo, request.pr_number)
        
        if not pr_data["files"]:
            raise HTTPException(400, "No files with changes found")
        
        print(f"📁 Found {len(pr_data['files'])} file(s)\n")
        
        # Initialize reviewer
        reviewer = AIReviewer()
        
        # Review files (max 3 for demo)
        reviews = []
        for i, file in enumerate(pr_data["files"][:3], 1):
            print(f"[{i}/3] Reviewing: {file['filename']}...")
            
            review = reviewer.review_code(file["filename"], file["patch"])
            
            reviews.append(ReviewResult(
                file=file["filename"],
                additions=file["additions"],
                deletions=file["deletions"],
                review=review
            ))
            
            print(f"✅ Complete\n")
        
        print(f"{'='*70}")
        print(f"✨ Review finished!")
        print(f"{'='*70}\n")
        
        return PRReviewResponse(
            status="completed",
            pr_title=pr_data["title"],
            pr_url=pr_data["url"],
            pr_author=pr_data["author"],
            files_reviewed=len(reviews),
            reviews=reviews
        )
    
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        raise HTTPException(500, str(e))
