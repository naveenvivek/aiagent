import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import uvicorn

# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")  # Placeholder - replace with your actual Groq API key

# FastAPI app
app = FastAPI(
    title="AI Agent API",
    description="A simple AI agent using LangChain and Groq",
    version="1.0.0"
)

# Pydantic models for request/response
class QueryRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = "You are a helpful AI assistant."
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class QueryResponse(BaseModel):
    response: str
    status: str

class AIAgent:
    """AI Agent class using LangChain and Groq"""
    
    def __init__(self, api_key: str):
        if api_key == "your-groq-api-key-here":
            raise ValueError("Please set your Groq API key in the GROQ_API_KEY environment variable")
        
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama3-8b-8192",  # Using Llama 3 8B model - you can also use "mixtral-8x7b-32768", "llama3-70b-8192"
            temperature=0.7
        )
    
    def query(self, message: str, system_prompt: str = "You are a helpful AI assistant.", 
              temperature: float = 0.7, max_tokens: int = 1000) -> str:
        """Query the LLM with a message and return the response"""
        try:
            # Update LLM parameters
            self.llm.temperature = temperature
            self.llm.max_tokens = max_tokens
            
            # Create messages
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=message)
            ]
            
            # Get response from LLM
            response = self.llm(messages)
            return response.content
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error querying LLM: {str(e)}")

# Initialize AI Agent (will be None if API key is not set)
ai_agent = None
try:
    ai_agent = AIAgent(GROQ_API_KEY)
except ValueError as e:
    print(f"Warning: {e}")
    print("The API will be available but will return errors until you set the API key.")

# FastAPI endpoints
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "AI Agent API is running",
        "status": "healthy",
        "api_key_configured": ai_agent is not None
    }

@app.post("/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
    """Query the AI agent with a message"""
    if ai_agent is None:
        raise HTTPException(
            status_code=503, 
            detail="AI Agent not initialized. Please set your Groq API key."
        )
    
    try:
        response = ai_agent.query(
            message=request.message,
            system_prompt=request.system_prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        return QueryResponse(
            response=response,
            status="success"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "ai_agent_initialized": ai_agent is not None,
        "groq_api_key_set": GROQ_API_KEY != "your-groq-api-key-here",
        "langchain_version": "0.3.25",
        "groq_version": "0.26.0"
    }

# Configuration endpoint to update API key (for development)
@app.post("/configure")
async def configure_api_key(api_key: str):
    """Configure the Groq API key (for development purposes)"""
    global ai_agent, GROQ_API_KEY
    
    try:
        GROQ_API_KEY = api_key
        ai_agent = AIAgent(api_key)
        return {"message": "API key configured successfully", "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to configure API key: {str(e)}")

if __name__ == "__main__":
    print("Starting AI Agent API...")
    print(f"API Key configured: {ai_agent is not None}")
    print("Access the API at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
