from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    user_message=req.message
    response= f"AI received: {user_message}"
    return{"response": response}