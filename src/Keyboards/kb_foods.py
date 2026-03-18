from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb_delete_food():
    kb = [
        [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник'), KeyboardButton(text='Среда')],
        [KeyboardButton(text='Четверг'), KeyboardButton(text='Пятница'), KeyboardButton(text='Суббота')],
        [KeyboardButton(text='Воскресенье'), KeyboardButton(text='Вся неделя')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_add_food():
    kb = [
        [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник'), KeyboardButton(text='Среда')],
        [KeyboardButton(text='Четверг'), KeyboardButton(text='Пятница'), KeyboardButton(text='Суббота')],
        [KeyboardButton(text='Воскресенье')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_add_food_name():
    kb = [
        [KeyboardButton(text='Завтрак'), KeyboardButton(text='Обед'), KeyboardButton(text='Ужин')],
        [KeyboardButton(text='Написать свое название приема пищи')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_delete_food_name(foods):
    kb = [[KeyboardButton(text=text) for text in foods[i * 3:(i + 3) * 3]] for i in range(len(foods) // 3 + 1)]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_add_food_calories(foods_all):
    pass
