from aiogram import Router
from aiogram import F
from aiogram.types import Message

from src.Keyboards.kb_mm import kb_setting

settings = Router()


@settings.message(F.text == 'Настройка')
async def settings_main(message: Message):
    await message.answer(
        '⚙️ Настройки питания\n\nЗдесь вы можете управлять своим рационом: создавать меню на день, редактировать время и состав приёмов пищи или удалять ненужное.\n\nВсе изменения сразу повлияют на ежедневные планы и напоминания, которые я вам присылаю.\n\nВыберите нужное действие:\n\n➕ Составить новое питание – задать блюда и время с нуля\n✏️ Редактировать существующее – изменить уже готовый план\n🗑️ Удалить питание – убрать приём пищи или полностью очистить расписание',
        reply_markup=kb_setting())
