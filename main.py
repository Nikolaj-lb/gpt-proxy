from fastapi import FastAPI
import openai
from pydantic import BaseModel
from typing import List, Dict
import os

# Инициализируем приложение FastAPI
app = FastAPI()


# Задайте свой API-ключ OpenAI
openai.api_key = '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'

# Модели для обработки запросов
class Message(BaseModel):
    role: str
    content: str
    
# Используем правильную модель запроса
class ChatRequest(BaseModel):
    messages: list[dict]

@app.post("/chat")
async def chat(request: ChatRequest):
    # Пример обработки сообщений
    response_message = "Привет, я бот! Я получил твое сообщение: " + request.messages[0].content
    return {"response": response_message}
