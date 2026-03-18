from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.Keyboards.kb_mm import kb_view
from src.State.states import ViewPlan

view = Router()

@view.message(F.text=='Просмотр')
async def view_main(message: Message, state: FSMContext):
    await message.answer('📅 За какой день показать план питания?', reply_markup=kb_view())
    await state.set_state(ViewPlan.day)

@view.message(ViewPlan.day)
async def view_get_day(message: Message, state: FSMContext):
    allow_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс', 'Вся неделя']
    if message.text.strip() in allow_days:
        pass # TODO: from bd get plan
    else:
        await message.answer('❌ Произошла ошибка, попробуйте еще раз')
        await state.clear()