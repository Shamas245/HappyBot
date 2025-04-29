import requests
import os
from dotenv import load_dotenv


load_dotenv()

GEMINI_KEY = os.environ.get('GEMINI_KEY')

response = requests.post(
    "https://api.aimlapi.com/v1/chat/completions",
    headers={
        "Content-Type": "application/json",

        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization": f"Bearer {GEMINI_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "google/gemini-2.0-flash-exp",
        "messages": [
            {
                "role": "user",

                # Insert your question for the model here, instead of Hello:
                "content": "How integrate FastAPI layout for Chat Safety Monitor"
            }
        ]
    }
)

data = response.json()
print(data)
