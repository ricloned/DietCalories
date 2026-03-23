from aiogram import Router
from aiogram.filters import CommandStart, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F

from src.Keyboards.kb_mm import kb_main_menu

main_menu = Router()


@main_menu.message(CommandStart())
async def message_with_text(message: Message):
    await message.answer(
        f"🌅 Доброе утро, {message.from_user.first_name}! Я — твой помощник по питанию.\n\nКаждое утро я буду присылать тебе план питания на сегодня, а в течение дня — напоминать о приёмах пищи, чтобы ты ничего не пропустил.\n\n<b>Чтобы я мог подстраиваться под твой режим, давай настроим твоё питание</b>:\n📋 Посмотреть всё питание — план приёмов пищи за сегодня / выбранный день.\n⚙️ Настроить питание — изменить расписание, блюда, порции.\n🔔 Управление уведомлениями — включить/отключить напоминания, изменить время.",
        reply_markup=kb_main_menu())
    from src.DataBase.Users.users import create_new_user
    create_new_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                    message.from_user.last_name)


@main_menu.message(F.text == "Главное меню")
async def message_with_text(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "🏠 Главное меню\n\nВыбери, что хочешь сделать:\n📋 Посмотреть всё питание — план приёмов пищи за сегодня / выбранный день.\n⚙️ Настроить питание — изменить расписание, блюда, порции.\n🔔 Управление уведомлениями — включить/отключить напоминания, изменить время.",
        reply_markup=kb_main_menu())
