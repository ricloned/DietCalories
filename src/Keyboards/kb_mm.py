from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb_main_menu():
    kb = [
        [KeyboardButton(text='Просмотр'), KeyboardButton(text='Настройка'), KeyboardButton(text='Уведомления')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_view():
    kb = [
        [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник'), KeyboardButton(text='Среда')],
        [KeyboardButton(text='Четверг'), KeyboardButton(text='Пятница'), KeyboardButton(text='Суббота')],
        [KeyboardButton(text='Воскресенье'), KeyboardButton(text='Вся неделя')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_setting():
    kb = [
        [KeyboardButton(text='Удалить план'), KeyboardButton(text='Составить план'), KeyboardButton(text='Изменить план')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_alarm():
    kb = [
        [KeyboardButton(text='Удалить уведомление'), KeyboardButton(text='Добавить уведомление')],
        [KeyboardButton(text='Изменить время уведомления')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)

