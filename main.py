from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import openai

app = FastAPI()

openai.OpenAI(api_key='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')

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[msg.dict() for msg in request.messages]
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

