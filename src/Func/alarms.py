from aiogram import Router
from aiogram import F
from aiogram.types import Message

from src.Keyboards.kb_mm import kb_alarm

alarm = Router()


@alarm.message(F.text == 'Уведомления')
async def alarm_main(message: Message):
    await message.answer(
        '🔔 Уведомления\n\nЗдесь вы можете управлять напоминаниями о приёмах пищи: добавлять новые, изменять существующие или удалять ненужные.\nЯ буду присылать вам уведомления в соответствии с этими настройками.\n\nВыберите действие:\n➕ Добавить уведомление — создать новое напоминание (например, завтрак, обед, ужин)\n✏️ Настроить существующее — изменить время, текст или дни повтора\n🗑️ Удалить уведомление — убрать конкретное напоминание или отключить все',
        reply_markup=kb_alarm())
