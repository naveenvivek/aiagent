# Simple AI Agent
# This is the main entry point for the AI agent

from agent import app
import uvicorn

def main():
    """Main entry point - starts the FastAPI server"""
    print("🚀 Starting AI Agent API Server...")
    print("📋 Features:")
    print("   - LangChain integration")
    print("   - OpenAI GPT models")
    print("   - FastAPI REST API")
    print("   - Interactive API docs")
    print()
    print("🌐 Server will be available at:")
    print("   - API: http://localhost:8000")
    print("   - Docs: http://localhost:8000/docs")
    print("   - Health: http://localhost:8000/health")
    print()
    print("⚠️  Don't forget to set your OpenAI API key!")
    print("   - Set OPENAI_API_KEY environment variable, or")
    print("   - Use the /configure endpoint")
    print()
    
    # Start the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    
if __name__ == "__main__":
    main()
