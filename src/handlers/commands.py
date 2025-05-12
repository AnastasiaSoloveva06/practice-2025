from telebot import TeleBot
from db import get_all_faq_keys

def setup_command_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        welcome_text = """👋 Привет! Я виртуальный помощник Московского политехнического университета..."""
        bot.send_message(message.chat.id, welcome_text)
    
    @bot.message_handler(commands=['faq'])
    def send_faq(message):
        faq_items = get_all_faq_keys()
        faq_text = "Часто задаваемые вопросы:\n\n" + "\n".join([f"▪️ {key.capitalize()}" for key in faq_items])
        bot.send_message(message.chat.id, faq_text + "\n\nНапиши интересующий вопрос, например 'расписание'")
