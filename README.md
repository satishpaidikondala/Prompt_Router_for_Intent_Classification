# AI Intent Router

An intelligently designed Python service that routes user requests to specialized AI personas using a two-step process: **Classify** and **Respond**.

## Overview
This system utilizes a lightweight LLM call to classify user intent and a second, more detailed call to generate a response from an "expert expert" persona tailored to that intent.

## Project Structure
```text
ai-intent-router/
├── main.py              # CLI Entry Point
├── README.md            # Documentation
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Container orchestration
├── route_log.jsonl     # Append-only JSON log of all requests
└── src/
    ├── __init__.py
    ├── api.py           # FastAPI REST Interface
    ├── classifier.py     # Intent detection logic
    ├── llm_client.py    # Centralized LLM connection
    ├── logger.py        # Logging utility
    ├── prompts.py       # Expert persona definitions
    └── router.py        # Routing and expert delegation
```

## Setup

### Environment Variables
Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

### Installation
Install dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface (CLI)
Run the interactive CLI:
```bash
python main.py
```
To run the pre-defined test battery:
```bash
python main.py --test
```

### Docker (REST API)
Build and run the service using Docker Compose:
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000`. You can test the routing endpoint:
```bash
curl -X POST "http://localhost:8000/route" -H "Content-Type: application/json" -d '{"message": "how do i sort a list in python?"}'
```

## Expert Personas
The system currently supports 4 distinct experts:
- **Code Expert**: Production-quality code and technical explanations.
- **Data Analyst**: Statistical insights and visualization suggestions.
- **Writing Coach**: Feedback on clarity, structure, and tone.
- **Career Advisor**: Actionable career advice and clarifying questions.

## Logging
Every request is logged to `route_log.jsonl` with the following schema:
```json
{
  "intent": "string",
  "confidence": "float",
  "user_message": "string",
  "final_response": "string"
}
```