#!/usr/bin/env python3
"""
Example usage of the AI Agent API
Run this after starting the agent.py server
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_query(message: str, system_prompt: str = None):
    """Test querying the AI agent"""
    print(f"💬 Testing query: '{message}'")
    
    payload = {"message": message}
    if system_prompt:
        payload["system_prompt"] = system_prompt
    
    try:
        response = requests.post(f"{BASE_URL}/query", json=payload)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {result['response']}")
        else:
            print(f"Error: {response.json()}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running!")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

def configure_api_key(api_key: str):
    """Configure the OpenAI API key"""
    print("🔑 Configuring API key...")
    try:
        response = requests.post(f"{BASE_URL}/configure", params={"api_key": api_key})
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

def main():
    print("🤖 AI Agent API Test Client")
    print("=" * 50)
    
    # Test health endpoint
    test_health()
    
    # Example queries (these will fail without API key)
    test_query("Hello! What's the weather like today?")
    test_query(
        "Explain quantum computing in simple terms",
        "You are a physics teacher explaining complex concepts to high school students."
    )
    
    print("💡 To use the API with OpenAI:")
    print("1. Get your API key from https://platform.openai.com/api-keys")
    print("2. Set environment variable: export OPENAI_API_KEY='your-key-here'")
    print("3. Or use the /configure endpoint with your API key")

if __name__ == "__main__":
    main()
