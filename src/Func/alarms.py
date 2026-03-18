from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.Keyboards.kb_alarms import kb_add_alarm
from src.Keyboards.kb_mm import kb_alarm
from src.State.states import AlarmsAdd

alarm = Router()


@alarm.message(F.text == 'Уведомления')
async def alarm_main(message: Message):
    await message.answer(
        '🔔 Уведомления\n\nЗдесь вы можете управлять напоминаниями о приёмах пищи: добавлять новые, изменять существующие или удалять ненужные.\nЯ буду присылать вам уведомления в соответствии с этими настройками.\n\nВыберите действие:\n➕ Добавить уведомление — создать новое напоминание (например, завтрак, обед, ужин)\n✏️ Настроить существующее — изменить время, текст или дни повтора\n🗑️ Удалить уведомление — убрать конкретное напоминание или отключить все',
        reply_markup=kb_alarm())

@alarm.message(F.text=='Удалить уведомление')
async def alarm_delete(message: Message, state:FSMContext):
    pass # TODO: get all alarms + add 'all' and then to kb and state

@alarm.message(F.text=='Добавить уведомление')
async def alarm_add(message: Message, state: FSMContext):
    pass # TODO: from db get all plans and to kb for choose
    await message.answer('Выберите название приема пищи снизу', reply_markup=kb_add_alarm())
    await state.set_state(AlarmsAdd.plan)

@alarm.message(AlarmsAdd.plan)
async def alarm_add_plan(message: Message, state: FSMContext):
    allow_plans = [] # TODO: from db get all plans and to kb for choose
    plan = message.text
    if plan in allow_plans:
        await state.update_data(plan=plan)
        await message.answer('Выберите день недели')


@alarm.message(F.text=='Изменить время уведомления')
async def alarm_change_time(message: Message, state: FSMContext):
    pass # TODO: get all alarms for change
