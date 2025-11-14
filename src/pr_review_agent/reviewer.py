from langchain_groq import ChatGroq
import os
from typing import Dict, List

class AIReviewer:
    """Multi-agent AI code reviewer using Groq"""
    
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        
        # Initialize Groq LLM
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=0.1,
            max_tokens=2000
        )
    
    def logic_agent_review(self, filename: str, patch: str) -> str:
        """Agent 1: Logic & Bug Analyzer"""
        prompt = f"""You are a Logic & Bug Analyzer with 15 years of debugging experience.

Analyze this code change for logic errors and bugs:

File: {filename}
Changes:

{patch}


Find and report (keep concise - max 500 words):
- Logic errors and incorrect conditionals
- Null pointer / undefined reference issues
- Off-by-one errors
- Race conditions
- Edge cases not handled

Format: Line X: [Issue] - Severity: High/Medium/Low
Provide fix suggestions."""
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in logic analysis: {str(e)}"
    
    def security_agent_review(self, filename: str, patch: str) -> str:
        """Agent 2: Security Auditor"""
        prompt = f"""You are a Security Auditor specializing in application security.

Audit this code change for vulnerabilities:

File: {filename}
Changes:


{patch}


Check for (keep concise - max 500 words):
- SQL injection, XSS, command injection
- Authentication/authorization bypass
- Sensitive data exposure
- Weak cryptography or password misuse
- Missing input validation

Format: Line X: [Vulnerability] - Risk: Critical/High/Medium
Explain how to exploit & mitigate."""
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in security analysis: {str(e)}"
    
    def performance_agent_review(self, filename: str, patch: str) -> str:
        """Agent 3: Performance Engineer"""
        prompt = f"""You are a Performance Engineer who optimizes high-traffic systems.

Evaluate this code change for performance issues:

File: {filename}
Changes:

{patch}

Look for (keep concise - max 500 words):
- Inefficient algorithms (O(n²), nested loops)
- N+1 database queries
- Memory leaks
- Blocking I/O
- Expensive unnecessary computations

Format: Line X: [Issue] - Impact: High/Medium/Low
Provide optimization ideas."""
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in performance analysis: {str(e)}"
    
    def quality_agent_review(self, filename: str, patch: str) -> str:
        """Agent 4: Code Quality Reviewer"""
        prompt = f"""You are a Code Quality Reviewer who wrote coding guidelines for Fortune 500 companies.

Review this code change:

File: {filename}
Changes:

{patch}


Check for (keep concise - max 500 words):
- Naming conventions
- Readability
- Maintainability
- Documentation
- Duplicate code
- Best practices & patterns

Format: Line X: [Suggestion]
Explain why improvement is needed."""
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in code quality analysis: {str(e)}"
    
    def review_code(self, filename: str, patch: str) -> List[Dict]:
        """Execute multi-agent review and return structured results"""
        
        print(f"\n🤖 Starting multi-agent review for {filename}...")
        
        # Store each agent's review separately
        agent_reviews = []
        
        # Agent 1: Logic Analysis
        print("  → Agent 1: Logic & Bug Analyzer...")
        logic_review = self.logic_agent_review(filename, patch)
        agent_reviews.append({
            "agent_name": "Logic & Bug Analyzer",
            "agent_role": "Identifies logic errors, bugs, and edge cases",
            "findings": logic_review,
            "issues_found": logic_review.count("Line")  # Simple count of issues
        })
        
        # Agent 2: Security Audit
        print("  → Agent 2: Security Auditor...")
        security_review = self.security_agent_review(filename, patch)
        agent_reviews.append({
            "agent_name": "Security Auditor",
            "agent_role": "Detects security vulnerabilities and risks",
            "findings": security_review,
            "issues_found": security_review.count("Line")
        })
        
        # Agent 3: Performance Analysis
        print("  → Agent 3: Performance Engineer...")
        performance_review = self.performance_agent_review(filename, patch)
        agent_reviews.append({
            "agent_name": "Performance Engineer",
            "agent_role": "Finds performance bottlenecks and inefficiencies",
            "findings": performance_review,
            "issues_found": performance_review.count("Line")
        })
        
        # Agent 4: Code Quality Review
        print("  → Agent 4: Code Quality Reviewer...")
        quality_review = self.quality_agent_review(filename, patch)
        agent_reviews.append({
            "agent_name": "Code Quality Reviewer",
            "agent_role": "Ensures maintainability and best practices",
            "findings": quality_review,
            "issues_found": quality_review.count("Line")
        })
        
        return agent_reviews  # RETURNS LIST OF AGENT REVIEWS
