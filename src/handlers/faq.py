from telebot import TeleBot
from db import search_in_faq

def setup_faq_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: search_in_faq(message.text))
    def handle_faq(message):
        answer = search_in_faq(message.text)
        if answer:
            bot.send_message(message.chat.id, answer)
