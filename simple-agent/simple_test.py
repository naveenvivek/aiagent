#!/usr/bin/env python3
"""
Simple test script for the AI Agent API
"""

import requests
import json

def test_api():
    base_url = "http://localhost:8000"
    
    print("🤖 Testing AI Agent API")
    print("=" * 40)
    
    # Test health endpoint
    print("1️⃣ Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status: {response.status_code}")
        health_data = response.json()
        print(f"   API Key Set: {health_data.get('openai_api_key_set')}")
        print(f"   Agent Initialized: {health_data.get('ai_agent_initialized')}")
        print()
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return
    
    # Test root endpoint
    print("2️⃣ Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        print()
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test query endpoint
    print("3️⃣ Testing query endpoint...")
    query_data = {
        "message": "What is 2+2? Please give a brief answer.",
        "temperature": 0.3,
        "max_tokens": 50
    }
    
    try:
        response = requests.post(f"{base_url}/query", json=query_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Success!")
            print(f"   Response: {result.get('response', 'No response')}")
        else:
            error_detail = response.json()
            print(f"   ❌ Error: {error_detail}")
            
            if "quota" in str(error_detail).lower():
                print("\n   💡 QUOTA ISSUE DETECTED:")
                print("   - Your OpenAI API key has exceeded its quota/credits")
                print("   - Check your billing at: https://platform.openai.com/usage")
                print("   - Add payment method at: https://platform.openai.com/settings/billing")
                print("   - Or use a different API key with available credits")
                
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n🔗 Useful Links:")
    print(f"   - API Docs: {base_url}/docs")
    print(f"   - Health Check: {base_url}/health")
    print("   - OpenAI Usage: https://platform.openai.com/usage")
    print("   - OpenAI Billing: https://platform.openai.com/settings/billing")

if __name__ == "__main__":
    test_api()
