from github import Github
from typing import Dict, List
import os

def get_pr_details(repo_name: str, pr_number: int) -> Dict:
    """Fetch PR details from GitHub"""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not found in .env file")
    
    try:
        g = Github(token)
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        files = []
        for file in pr.get_files():
            if file.patch:  # Only files with actual code changes
                files.append({
                    "filename": file.filename,
                    "status": file.status,
                    "additions": file.additions,
                    "deletions": file.deletions,
                    "patch": file.patch
                })
        
        return {
            "title": pr.title,
            "description": pr.body or "No description provided",
            "author": pr.user.login,
            "url": pr.html_url,
            "files": files,
            "state": pr.state
        }
    
    except Exception as e:
        raise Exception(f"Error fetching PR: {str(e)}")
