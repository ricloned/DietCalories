from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.Keyboards.kb_foods import kb_delete_food, kb_add_food, kb_add_food_name
from src.Keyboards.kb_mm import kb_setting
from src.State.states import SettingsDelete, SettingsAdd

settings = Router()


@settings.message(F.text == 'Настройка')
async def setting_main(message: Message):
    await message.answer(
        '⚙️ Настройки питания\n\nЗдесь вы можете управлять своим рационом: создавать меню на день, редактировать время и состав приёмов пищи или удалять ненужное.\n\nВсе изменения сразу повлияют на ежедневные планы и напоминания, которые я вам присылаю.\n\nВыберите нужное действие:\n\n➕ Составить новое питание – задать блюда и время с нуля\n✏️ Редактировать существующее – изменить уже готовый план\n🗑️ Удалить питание – убрать приём пищи или полностью очистить расписание',
        reply_markup=kb_setting())


@settings.message(F.text == 'Удалить план')
async def setting_delete(message: Message, state: FSMContext):
    await message.answer("📅 За какой день удалить план питания?", reply_markup=kb_delete_food())
    await state.set_state(SettingsDelete.day)

@settings.message(SettingsDelete.day)
async def setting_delete_day(message: Message, state: FSMContext):
    allow_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье', 'Вся неделя']
    if message.text.strip() in allow_days:
        pass  # TODO: from bd get plan
    else:
        await message.answer('❌ Произошла ошибка, попробуйте еще раз')
        await state.clear()

@settings.message(F.text=='Составить план')
async def setting_add(message: Message, state: FSMContext):
    await message.answer('📅 На какой день добавить план питания?', reply_markup=kb_add_food())
    await state.set_state(SettingsAdd.day)

@settings.message(SettingsAdd.day)
async def setting_add_day(message: Message, state: FSMContext):
    allow_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if message.text.strip() in allow_days:
        await state.update_data(day=message.text.strip())
        await message.answer('Выберите или напиши название приема пищи', reply_markup=kb_add_food_name())
        await state.set_state(SettingsAdd.meals)
    else:
        await message.answer('❌ Произошла ошибка, попробуйте еще раз')
        await state.clear()

@settings.message(SettingsAdd.meals)
async def setting_add_meals(message: Message, state: FSMContext):
    await message.answer('Укажите название еду')
    meals = message.text
    await state.update_data(meals=meals)
    await state.set_state(SettingsAdd.plan)

@settings.message(SettingsAdd.plan)
async def setting_add_plan(message: Message, state: FSMContext):
    plan = message.text
    await state.update_data(plan=plan)
    # TODO: func DataBase.Foods get state and then adds in db if good say good if bad say bad


@settings.message(F.text=='Изменить план')
async def change_meals(message: Message, state: FSMContext):
    pass # TODO: get from db all meals and to kb for choose

