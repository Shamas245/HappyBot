from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    role = str


@app.get('/question')
def ask(question: str):
    return question


@app.get('/answer')
def response(answer: str):
    return answer
