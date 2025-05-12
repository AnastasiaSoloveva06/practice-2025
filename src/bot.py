import telebot
from gigachat import GigaChat
from typing import Dict, List

# Конфигурация
TELEGRAM_TOKEN = "7873995348:AAEjGD5wrvGoYcgBLQoaRCBmXg0fxluxLL8"
GIGACHAT_AUTH = "NjkzMTM4MzAtZjY1Zi00NzI4LWFjZmMtYTZlOTRiMGU2OTFiOjMxNTcxNGMzLWRmN2EtNGQ5YS1hNzE5LWU2YWVmODljODc0OQ=="

# Инициализация
bot = telebot.TeleBot(TELEGRAM_TOKEN)
giga = GigaChat(credentials=GIGACHAT_AUTH, verify_ssl_certs=False)

# База данных FAQ с реальными ссылками
FAQ = {
    "расписание": "Актуальное расписание доступно на сайте: https://rasp.dmami.ru/site/",
    "контакты": """
Основные контакты Мосполитеха:
📞 Приёмная комиссия: +7 (495) 223-05-23
🌐 Сайт: https://mospolytech.ru
📍 Адрес: г. Москва, ул. Большая Семёновская, 38
    """,
    "поступление": """
Информация о поступлении:
- Бакалавриат/специалитет: https://mospolytech.ru/postupayushchim/programmy-obucheniya/
- Магистратура: https://mospolytech.ru/postupayushchim/programmy-obucheniya/magistratura/
- Аспирантура: https://mospolytech.ru/postupayushchim/programmy-obucheniya/aspirantura-i-doktorantura/
    """,
    "общежитие": """
Информация об общежитиях:
- Правила проживания: https://mospolytech.ru/obschejitiya/#pravila
- Контакты:https://mospolytech.ru/obschejitiya/
    """,
    "стипендия": """
Информация о стипендиях:
- Виды стипендий: https://profkommospolytech.ru/privilege/
- Размеры выплат: http://profkommospolytech.ru/privilege
    """,
    "учебные материалы": """
Учебные материалы можно найти:
- В электронной библиотеке: https://mospolytech.ru/obuchauschimsya/biblioteka/
- На сайте кафедры соответствующей дисциплины
- В LMS системе университета
    """
}

# Системный промпт для GigaChat
SYSTEM_PROMPT = """
Ты - ассистент Московского политехнического университета. 
Отвечай только на вопросы, связанные с университетом. 
Используй только официальные источники с сайта Мосполитеха. 
Если вопрос не связан с университетом, вежливо откажись отвечать.
Официальный сайт: https://mospolytech.ru
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
👋 Привет! Я виртуальный помощник Московского политехнического университета.

Я могу помочь с:
🔹 Расписанием занятий
🔹 Контактами университета
🔹 Учебными материалами
🔹 Часто задаваемыми вопросами

Используй команды:
/rasp - Расписание
/contacts - Контакты
/faq - Частые вопросы
/materials - Учебные материалы
    """
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
Доступные команды:
/start - Начало работы
/rasp - Поиск расписания
/contacts - Контакты университета
/faq - Часто задаваемые вопросы
/materials - Поиск учебных материалов
    """
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['rasp'])
def send_schedule(message):
    bot.send_message(message.chat.id, "Актуальное расписание занятий доступно на сайте: https://rasp.dmami.ru/site/")

@bot.message_handler(commands=['contacts'])
def send_contacts(message):
    bot.send_message(message.chat.id, FAQ['контакты'])

@bot.message_handler(commands=['faq'])
def send_faq(message):
    faq_text = "Часто задаваемые вопросы:\n\n" + "\n".join([f"▪️ {key.capitalize()}" for key in FAQ.keys()])
    bot.send_message(message.chat.id, faq_text + "\n\nНапиши интересующий вопрос, например 'расписание'")

@bot.message_handler(commands=['materials'])
def send_materials(message):
    bot.send_message(message.chat.id, FAQ['учебные материалы'])

@bot.message_handler(func=lambda message: message.text.lower() in FAQ)
def handle_faq(message):
    bot.send_message(message.chat.id, FAQ[message.text.lower()])

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if any(word in message.text.lower() for word in ['политех', 'моспол', 'универ', 'мосполитех', 'Московский политех']):
        response = ask_gigachat(message.text)
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Я отвечаю только на вопросы, связанные с Московским политехническим университетом.")

def ask_gigachat(prompt: str) -> str:
    try:
        response = giga.chat(
            f"{SYSTEM_PROMPT}\n\nВопрос: {prompt}\n\nОтвет должен содержать только информацию с официальных источников Мосполитеха."
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при обработке запроса: {str(e)}"

if __name__ == '__main__':
    print("Бот Московского политеха запущен...")
    bot.p
