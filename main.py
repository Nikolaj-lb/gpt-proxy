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
    messages: list

@app.post("/chat")
async def chat(request: ChatRequest):
    # Убедитесь, что ключ API правильно задан
    # Задайте свой API-ключ OpenAI
    openai.api_key = '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'

    
    # Запрос к OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Вы можете использовать другую модель, если нужно
        messages=request.messages
    )
    
    # Отправляем ответ от модели
    return {"response": response.choices[0].message["content"]}
