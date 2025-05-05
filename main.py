from fastapi import FastAPI
import openai
from pydantic import BaseModel
from typing import List, Dict
import os

# Инициализируем приложение FastAPI
app = FastAPI()


# Задайте свой API-ключ OpenAI
openai.api_key = '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'


# Используем правильную модель запроса
class ChatRequest(BaseModel):
    messages: list[dict]

@app.post("/chat")
async def chat(request: ChatRequest):
    # Пример того, как получить и обработать сообщение из запроса
    user_message = request.messages[0]['content']
    return {"response": f"Ты сказал: {user_message}"}
