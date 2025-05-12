from gigachat import GigaChat
from config import GIGACHAT_AUTH, SYSTEM_PROMPT
import os

giga = GigaChat(credentials=os.getenv('GIGACHAT_AUTH') or GIGACHAT_AUTH, verify_ssl_certs=False)

def ask_gigachat(prompt: str) -> str:
    try:
        response = giga.chat(
            f"{SYSTEM_PROMPT}\n\nВопрос: {prompt}\n\nОтвет должен содержать только информацию с официальных источников."
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при обработке запроса: {str(e)}"
