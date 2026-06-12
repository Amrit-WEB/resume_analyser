from pydantic import BaseModel
# from openai import OpenAI
from google import genai
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import os
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# client = OpenAI(
#     api_key = os.getenv("OPEN_AI_API_KEY")
# )
client = genai.Client(
    api_key= os.getenv("GEMINI_AI_API_KEY")
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

    # FOR OPEN AI
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": req.message
    #         }
    #     ]
    # )

    # return {
    #     "answer": response.choices[0].message.content
    # }

    #FOR GEMINI AI
    print("Received message:", req.message)  # Debugging statement
    response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents=req.message,
    )

    return {
        "answer": response.text
    }