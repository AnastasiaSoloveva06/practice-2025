# Токены и конфигурация
TELEGRAM_TOKEN = "7873995348:AAEjGD5wrvGoYcgBLQoaRCBmXg0fxluxLL8"
GIGACHAT_AUTH = "NjkzMTM4MzAtZjY1Zi00NzI4LWFjZmMtYTZlOTRiMGU2OTFiOjMxNTcxNGMzLWRmN2EtNGQ5YS1hNzE5LWU2YWVmODljODc0OQ=="

# Системный промпт для GigaChat
SYSTEM_PROMPT = """
Ты - ассистент Московского политехнического университета. 
Отвечай только на вопросы, связанные с университетом. 
Используй только официальные источники с сайта Мосполитеха. 
Если вопрос не связан с университетом, вежливо откажись отвечать.
Официальный сайт: https://mospolytech.ru
"""

# База данных FAQ
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
