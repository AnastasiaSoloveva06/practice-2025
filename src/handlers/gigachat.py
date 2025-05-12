from telebot import TeleBot
from services.gigachat_service import ask_gigachat

def setup_gigachat_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda m: True)
    def handle_message(message):
        if any(word in message.text.lower() for word in ['политех', 'моспол', 'универ']):
            response = ask_gigachat(message.text)
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Я отвечаю только на вопросы, связанные с университетом.")
