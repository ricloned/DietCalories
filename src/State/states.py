from aiogram.fsm.state import StatesGroup, State


class ViewPlan(StatesGroup):
    day = State()