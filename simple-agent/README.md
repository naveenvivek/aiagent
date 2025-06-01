# Simple AI Agent

A FastAPI-based AI agent using LangChain and Groq's fast inference API with Llama models.

## Features

- 🤖 **LangChain Integration**: Leverages LangChain for robust LLM interactions
- ⚡ **Groq Fast Inference**: Uses Groq's lightning-fast LLM inference
- 🦙 **Llama Models**: Access to Llama 3 8B, 70B, and Mixtral models
- 🚀 **FastAPI**: Modern, fast web framework with automatic API documentation
- 📝 **Interactive API Docs**: Built-in Swagger UI for easy testing
- 🔧 **Configurable**: Customizable system prompts, temperature, and token limits

## Setup

### 1. Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

You have several options to set your OpenAI API key:

**Option A: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

**Option B: Use the /configure endpoint**
After starting the server, send a POST request to `/configure` with your API key.

### 3. Start the Server

```bash
python main.py
```

Or run the agent directly:
```bash
python agent.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### GET `/`
Health check endpoint
```json
{
  "message": "AI Agent API is running",
  "status": "healthy",
  "api_key_configured": true
}
```

### POST `/query`
Query the AI agent with a message

**Request:**
```json
{
  "message": "Hello! What's the weather like today?",
  "system_prompt": "You are a helpful AI assistant.",
  "temperature": 0.7,
  "max_tokens": 1000
}
```

**Response:**
```json
{
  "response": "I'm an AI assistant and I don't have access to real-time weather data...",
  "status": "success"
}
```

### GET `/health`
Detailed health check with configuration status

### POST `/configure`
Configure the OpenAI API key (for development)

## Usage Examples

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Query the agent
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Explain quantum computing",
       "system_prompt": "You are a physics teacher"
     }'
```

### Using Python

```python
import requests

# Query the agent
response = requests.post("http://localhost:8000/query", json={
    "message": "What is machine learning?",
    "temperature": 0.5
})

print(response.json()["response"])
```

### Using the Test Client

Run the included test client:
```bash
python test_api.py
```

## Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Configuration

### Model Settings
- **Model**: GPT-3.5-turbo (changeable in `agent.py`)
- **Temperature**: 0.7 (adjustable per request)
- **Max Tokens**: 1000 (adjustable per request)

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key

## Project Structure

```
simple-agent/
├── agent.py          # Main AI agent with FastAPI
├── main.py           # Entry point
├── test_api.py       # API test client
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── venv/            # Virtual environment (ignored by git)
```

## Getting Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Sign up or log in
3. Navigate to [API Keys](https://platform.openai.com/api-keys)
4. Create a new secret key
5. Copy and use it in your environment

## Troubleshooting

### API Key Issues
- Make sure your API key is valid and has sufficient credits
- Check that the key is properly set in environment variables
- Use the `/health` endpoint to verify configuration

### Connection Issues
- Ensure the server is running on port 8000
- Check firewall settings
- Verify no other service is using port 8000

### Model Access
- GPT-4 requires special access - use GPT-3.5-turbo if you don't have it
- Check your OpenAI usage limits and billing

## Contributing

Feel free to submit issues and enhancement requests!
