from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx
import os

app = FastAPI()

# Получаем API-ключ из переменной окружения
OPENROUTER_API_KEY = "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"

# Модель входящего сообщения
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat")
async def chat(request: ChatRequest):
    if not OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="OpenRouter API key is not set")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",  # Замени на свой домен или localhost
        "X-Title": "GPT Proxy App"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # Можно сменить на другую модель
        "messages": [msg.dict() for msg in request.messages]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        answer = data["choices"][0]["message"]["content"]
        return {"response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

