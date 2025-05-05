from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

# Устанавливаем API-ключ из переменной окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages")  # Извлекаем список сообщений
    if not messages:
        return JSONResponse(content={"error": "Missing 'messages'"}, status_code=400)

    try:
        # Отправляем запрос в OpenAI API с использованием модели gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Модель для чатов
            messages=messages         # Передаем сообщения
        )
        # Возвращаем ответ от модели
        return JSONResponse(content=response['choices'][0]['message'])
    except Exception as e:
        # В случае ошибки возвращаем ее описание
        return JSONResponse(content={"error": str(e)}, status_code=500)

