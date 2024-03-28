from aiogram.fsm.state import StatesGroup, State


class PhoneRequest(StatesGroup):
    phone = State()

