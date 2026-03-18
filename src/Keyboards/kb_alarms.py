from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_add_alarm():
    kb = [
        [KeyboardButton(text='Завтрак'), KeyboardButton(text='Обед'), KeyboardButton(text='Ужин')],
        [KeyboardButton(text='Написать свое название приема пищи')],
        [KeyboardButton(text='Главное меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_delete_alarm(alarms):
    kb = [[KeyboardButton(text=text) for text in alarms[i * 3:(i + 1) * 3]] for i in
          range(len(alarms) // 3 + 1)]  # not right + all alarms
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)


def kb_change_alarm(alarms):
    kb = [[KeyboardButton(text=text) for text in alarms[i * 3:(i + 1) * 3]] for i in
          range(len(alarms) // 3 + 1)]  # not right + all alarms
    return ReplyKeyboardMarkup(keyboard=kb, resize=True)