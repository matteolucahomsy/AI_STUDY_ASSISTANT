from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()
print(repr(os.getenv("OPENAI_API_KEY")))
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    print("Message:", req.message)
    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful study assistant for students."},
                {"role": "user", "content": req.message}
            ]
        )
        ai=response.choices[0].message.content
        print("AI:" , ai)
        return {"response": ai}
    except Exception as e:
        print("OPENAI ERROR:", e)
        return {"response": "error: " + str(e)}
    
    