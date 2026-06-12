from pydantic import BaseModel
from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv

import os
load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key = os.getenv("OPEN_AI_API_KEY")
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "msg":"hi, there. how are you"
    }

@app.post("/chat")
def chat(req: ChatRequest):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": req.message
            }
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }