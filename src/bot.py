import telebot
from telebot import types
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
- Контакты: https://mospolytech.ru/obschejitiya/
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

# Создаем главное меню
def create_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton('Расписание'),
        types.KeyboardButton('Контакты'),
        types.KeyboardButton('Поступление'),
        types.KeyboardButton('Общежитие'),
        types.KeyboardButton('Стипендия'),
        types.KeyboardButton('Учебные материалы'),
        types.KeyboardButton('Помощь')
    ]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
👋 Привет! Я виртуальный помощник Московского политехнического университета.

Я могу помочь с:
🔹 Расписанием занятий
🔹 Контактами университета
🔹 Поступлением
🔹 Общежитием
🔹 Стипендиями
🔹 Учебными материалами

Выберите нужный раздел или задайте вопрос:
    """
    bot.send_message(message.chat.id, welcome_text, reply_markup=create_main_keyboard())

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
ℹ️ Доступные команды:
/start - Начало работы
/help - Помощь по боту

Основные разделы:
• Расписание - Актуальное расписание занятий
• Контакты - Контактная информация университета
• Поступление - Информация для абитуриентов
• Общежитие - Информация о студенческих общежитиях
• Стипендия - Виды и условия получения стипендий
• Учебные материалы - Доступ к учебным ресурсам

Вы также можете задать вопрос в свободной форме.
    """
    bot.send_message(message.chat.id, help_text, reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()
    
    if text in ['расписание', '/rasp']:
        bot.send_message(message.chat.id, FAQ['расписание'])
    elif text in ['контакты', '/contacts']:
        bot.send_message(message.chat.id, FAQ['контакты'])
    elif text in ['поступление']:
        bot.send_message(message.chat.id, FAQ['поступление'])
    elif text in ['общежитие']:
        bot.send_message(message.chat.id, FAQ['общежитие'])
    elif text in ['стипендия']:
        bot.send_message(message.chat.id, FAQ['стипендия'])
    elif text in ['учебные материалы', 'материалы']:
        bot.send_message(message.chat.id, FAQ['учебные материалы'])
    elif text in ['помощь', '/help']:
        send_help(message)
    elif text in FAQ:
        bot.send_message(message.chat.id, FAQ[text])
    else:
        if any(word in text for word in ['политех', 'моспол', 'универ', 'мосполитех', 'московский политех']):
            try:
                response = ask_gigachat(message.text)
                bot.send_message(message.chat.id, response)
            except Exception as e:
                bot.send_message(message.chat.id, "⚠️ Произошла ошибка при обработке запроса. Пожалуйста, попробуйте позже.")
        else:
            bot.send_message(message.chat.id, "Я отвечаю только на вопросы, связанные с Московским политехническим университетом.", reply_markup=create_main_keyboard())

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
    bot.polling(none_stop=True)
