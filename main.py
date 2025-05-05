from fastapi import FastAPI
import openai
from pydantic import BaseModel
from typing import List, Dict
import os

# Инициализируем приложение FastAPI
app = FastAPI()


# Задайте свой API-ключ OpenAI
openai.api_key = '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'


# Модель для получения запроса
class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Отправляем запрос в OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Модель для обработки
            messages=request.messages   # Данные сообщений из запроса
        )
        return {"response": response['choices'][0]['message']['content']}
    except Exception as e:
        return {"error": str(e)}
