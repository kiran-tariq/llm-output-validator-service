import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:4b",
        "prompt": "Say hello in one sentence.",
        "stream": False
    },
    timeout=600
)

print(response.status_code)
print(response.json())s