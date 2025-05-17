from telebot import TeleBot
from db import get_all_faq_keys

# Приветственное сообщение
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """
<b>👋 Добро пожаловать в бота Мосполитеха!</b>

Я помогу найти актуальную информацию:
• Расписание занятий
• Контакты университета
• Учебные материалы
• Частые вопросы

<b>Используйте кнопки ниже ↓</b>
"""
    bot.send_message(message.chat.id, welcome_text, 
                   parse_mode='HTML', 
                   reply_markup=make_main_keyboard())

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    
    if 'распис' in text:
        bot.send_message(message.chat.id, FAQ['расписание'], parse_mode='HTML', disable_web_page_preview=True)
    elif 'контакт' in text:
        bot.send_message(message.chat.id, FAQ['контакты'], parse_mode='HTML', disable_web_page_preview=True)
    elif 'учебн' in text or 'материал' in text:
        bot.send_message(message.chat.id, FAQ['учебные материалы'], parse_mode='HTML')
    elif 'faq' in text or 'частые' in text or 'вопросы' in text:
        bot.send_message(message.chat.id, "🔍 <b>Часто задаваемые вопросы:</b>", 
                        parse_mode='HTML', reply_markup=make_faq_keyboard())
    else:
        if any(word in text for word in ['политех', 'моспол', 'универ']):
            try:
                bot.send_chat_action(message.chat.id, 'typing')
                response = giga.chat(f"Ты помощник Мосполитеха. Ответь кратко на русском: {message.text}")
                bot.send_message(message.chat.id, f"<i>{response.choices[0].message.content}</i>", parse_mode='HTML')
            except:
                bot.send_message(message.chat.id, "⚠️ Ошибка обработки запроса. Попробуйте позже.")
        else:
            bot.send_message(message.chat.id, "Я отвечаю только на вопросы, связанные с Московским политехническим университетом. Для удобства используйте кнопки меню для навигации.")

# Обработчик inline-кнопок FAQ
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith('faq_'):
        faq_type = call.data.split('_')[1]
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, FAQ[faq_type], parse_mode='HTML')
    elif call.data == 'main_menu':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        start(call.message)
    
    bot.answer_callback_query(call.id)
