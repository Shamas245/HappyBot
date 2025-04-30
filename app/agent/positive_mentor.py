import requests
from fastapi import FastAPI
from config import load_gemini


app = FastAPI()
load_gemini()


@app.get('/chat')
def ask(prompt: str):
    response = requests.post(
        "https://api.aimlapi.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",

            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": f"Bearer {load_gemini()}",
            "Content-Type": "application/json"
        },
        json={
            "model": "google/gemini-2.0-flash-exp",
            "messages": [
                {
                    "role": "user",

                    # Insert your question for the model here, instead of Hello:
                    "content": f"{prompt}"
                }
            ]
        }
    )

    data = response.json()
    return data
