from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Задайте свой API-ключ OpenAI
openai.api_key = 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


app = FastAPI()

# Модель для получения запроса от пользователя
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the GPT Proxy!"}

@app.post("/chat")
async def chat(request: ChatRequest):
    # Обработка запроса от пользователя
    user_message = request.messages[-1].content  # Последнее сообщение от пользователя
    
    # Отправка запроса в OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Вы можете изменить на любой доступный GPT-модель
            messages=[{"role": "user", "content": user_message}],
        )
        
        answer = response['choices'][0]['message']['content']
        return {"response": answer}

    except Exception as e:
        return {"error": str(e)}
