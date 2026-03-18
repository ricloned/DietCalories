from aiogram.fsm.state import StatesGroup, State


class ViewPlan(StatesGroup):
    day = State()


class SettingsDelete(StatesGroup):
    day = State()


class SettingsAdd(StatesGroup):
    day = State()
    meals = State()
    plan = State()

class AlarmsAdd(StatesGroup):
    plan = State()