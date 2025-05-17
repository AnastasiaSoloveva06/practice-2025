from typing import Dict

FAQ = {
    "расписание": "📅 <b>Актуальное расписание занятий</b>\n\n🔹 Сайт с расписанием: <a href='https://rasp.dmami.ru/site/'>rasp.dmami.ru</a>\n🔹 Мобильное приложение: <i>доступно в AppStore и Google Play</i>",
    "контакты": "📞 <b>Контактная информация</b>\n\n🏛 <b>Приёмная комиссия:</b> +7 (495) 223-05-23\n🌐 <b>Официальный сайт:</b> <a href='https://mospolytech.ru'>mospolytech.ru</a>\n🗺 <b>Адрес:</b> <a href='https://yandex.ru/maps/-/CHv0fVYW'>ул. Большая Семёновская, 38</a>",
    "поступление": "🎓 <b>Информация о поступлении</b>\n\n➡️ <b>Бакалавриат/Специалитет:</b> <a href='https://mospolytech.ru/postupayushchim/'>Подробнее</a>\n➡️ <b>Магистратура:</b> <a href='https://mospolytech.ru/postupayushchim/programmy-obucheniya/magistratura/'>Подробнее</a>\n➡️ <b>Аспирантура:</b> <a href='https://mospolytech.ru/obuchauschimsya/aspirantura/'>Подробнее</a>",
    "общежитие": "🏢 <b>Общежития</b>\n\n🔹 <a href='https://mospolytech.ru/obschejitiya/'>Общая информация</a>\n🔹 <a href='https://mospolytech.ru/obschejitiya/poryadok-oformleniya-dokumentov/'>Порядок оформления документов</a>",
    "стипендия": "💰 <b>Стипендии</b>\n\n🔹 <a href='https://profkommospolytech.ru/privilege/'>Виды и условия получения</a>\n\n<i>Актуальные размеры выплат уточняйте на сайте</i>",
    "учебные материалы": "📚 <b>Учебные материалы</b>\n\n🔹 <a href='https://mospolytech.ru/obuchauschimsya/biblioteka/'>Электронная библиотека</a>\n🔹 LMS система: <i>доступ после авторизации</i>",
    "военнообязанным": "🎖 <b>Военнообязанным</b>\n\n🔹 <a href='https://mospolytech.ru/obuchauschimsya/voennoobyazannym-i-prizyvnikam/'>Информация для призывников</a>",
    "студенческая жизнь": "🌟 <b>Студенческая жизнь</b>\n\n🔹 <a href='https://mospolytech.ru/studencheskaya-zhizn/o-studencheskoy-jizni/'>Мероприятия и клубы/секции</a>"
}

def get_faq_item(key: str) -> str:
    """Получить ответ из FAQ по ключу"""
    return FAQ_DATABASE.get(key.lower(), "Информация по данному вопросу не найдена.")

def get_all_faq_keys() -> list:
    """Получить список всех доступных вопросов в FAQ"""
    return list(FAQ_DATABASE.keys())

def search_in_faq(query: str) -> str:
    """Поиск по FAQ с проверкой вхождения запроса в ключи"""
    query = query.lower()
    for key in FAQ_DATABASE:
        if query in key:
            return FAQ_DATABASE[key]
    return None
