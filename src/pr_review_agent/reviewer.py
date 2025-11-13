from langchain_groq import ChatGroq
import os

class AIReviewer:
    """AI-powered code reviewer using Groq"""
    
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=0.1,
            max_tokens=2000
        )
    
    def review_code(self, filename: str, patch: str) -> str:
        """Generate comprehensive code review"""
        
        # This is the prompt - it's just a string variable
        prompt = f"""You are an expert code reviewer. Analyze this code change thoroughly.

**File:** {filename}
**Code Changes:**
{patch}

Provide a comprehensive review covering:

## 🔍 Logic & Bugs
- Check for logic errors, edge cases, and potential bugs
- Identify null pointer issues or incorrect conditionals
- Format: `Line X: [Issue] - Severity: High/Medium/Low`

## 🔒 Security
- Look for SQL injection, XSS, or authentication vulnerabilities
- Check for data exposure or insecure practices
- Format: `Line X: [Vulnerability] - Risk: Critical/High/Medium`

## ⚡ Performance
- Identify inefficient algorithms or database queries
- Check for memory leaks or unnecessary operations
- Format: `Line X: [Issue] - Impact: High/Medium/Low`

## ✨ Code Quality
- Review naming conventions and documentation
- Check code complexity and maintainability
- Suggest improvements following best practices

Be specific, actionable, and cite line numbers from the diff."""

        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error during review: {str(e)}"
