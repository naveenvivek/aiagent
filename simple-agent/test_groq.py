#!/usr/bin/env python3
"""
Simple test script for Groq AI Agent
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_groq_agent():
    """Test the Groq AI agent"""
    print("🚀 Testing Groq AI Agent")
    print("=" * 50)
    
    # Test health endpoint
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running!")
        return
    
    # Test query endpoint
    print("💬 Testing query with Llama 3...")
    query_data = {
        "message": "Explain the concept of machine learning in simple terms.",
        "system_prompt": "You are a helpful AI assistant that explains complex topics clearly.",
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(f"{BASE_URL}/query", json=query_data)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Response: {result['response']}")
        else:
            print(f"❌ Error: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("💡 To use Groq:")
    print("1. Get your API key from https://console.groq.com/keys")
    print("2. Set environment variable: export GROQ_API_KEY='your-key-here'")
    print("3. Or use the /configure endpoint with your API key")
    print("\n🎯 Available Groq models:")
    print("- llama3-8b-8192 (default)")
    print("- llama3-70b-8192")
    print("- mixtral-8x7b-32768")

if __name__ == "__main__":
    test_groq_agent()
