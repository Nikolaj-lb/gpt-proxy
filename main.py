from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages")
    if not messages:
        return JSONResponse(content={"error": "Missing 'messages'"}, status_code=400)

    try:
        # Новый способ работы с Chat API начиная с версии openai>=1.0.0
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Используем модель gpt-3.5-turbo
            messages=messages  # Передаем все сообщения как список
        )
        return JSONResponse(content=response['choices'][0]['message'])
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


