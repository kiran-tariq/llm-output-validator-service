# LLM Output Validator Service

A FastAPI-based service that validates Large Language Model (LLM) outputs against predefined Pydantic schemas. The service automatically retries invalid responses, logs validation metrics in SQLite, and exposes interactive API documentation through Swagger.

---

## Features

- Validate LLM outputs using **Pydantic v2**
- Automatic retry loop for invalid responses
- Local LLM integration using **Ollama (Qwen 3)**
- FastAPI REST API
- SQLite metrics logging
- Interactive Swagger documentation
- Multiple validation schemas
- Structured JSON responses

---

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic v2
- SQLAlchemy
- SQLite
- Ollama
- Qwen3:4B
- Uvicorn

---

## Project Structure

```
llm_output_validator/
│
├── app/
│   ├── main.py
│   ├── validator.py
│   ├── llm_client.py
│   ├── schemas.py
│   ├── database.py
│   ├── models.py
│   └── metrics.py
│
├── tests/
├── logs/
├── requirements.txt
├── README.md
└── validator.db
```

---

## API Endpoints

### POST `/validate`

Validates an LLM response against the selected schema.

Example Request

```json
{
  "prompt": "Analyze sentiment: I love this phone",
  "schema_name": "sentiment"
}
```

Example Response

```json
{
  "success": true,
  "attempts": 3,
  "data": {
    "sentiment": "positive",
    "confidence": 0.95,
    "explanation": "The phrase expresses strong positive sentiment."
  }
}
```

---

### GET `/metrics`

Returns validation statistics including:

- Total API calls
- Success rate
- Average retry attempts
- Common validation errors

---

### GET `/schemas`

Lists all available validation schemas supported by the service.

---

## Validation Workflow

```
User Prompt
      │
      ▼
 Local LLM (Qwen via Ollama)
      │
      ▼
Pydantic Validation
      │
      ├─────────────── Valid
      │                   │
      ▼                   ▼
Retry with Error      Return Result
Feedback (up to 3x)
```

---

## Available Schemas

- SentimentResult
- TaskExtraction
- ContentSummary

---

## Running the Project

### Clone Repository

```bash
git clone https://github.com/your-username/llm-output-validator-service.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama run qwen3:4b
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

to test the API interactively.

---

## Skills Demonstrated

- FastAPI API Development
- LLM Integration
- Pydantic Validation
- Structured Output Enforcement
- Retry Logic
- Error Handling
- SQLAlchemy ORM
- SQLite Database
- REST APIs
- AI Reliability Engineering

---

## Future Improvements

- Dynamic schema creation
- Response caching
- Authentication
- Docker support
- Cloud deployment (Render/Railway)

---

## Author

**Kiran Tariq**

GitHub: https://github.com/kiran-tariq
