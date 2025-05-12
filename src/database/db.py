from typing import Dict

# База данных FAQ с реальными ссылками
FAQ_DATABASE = {
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
