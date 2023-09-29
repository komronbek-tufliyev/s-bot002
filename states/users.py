from aiogram.dispatcher.filters.state import State, StatesGroup


class UserForm(StatesGroup):
    phone = State()
    full_name = State()
    workplace = State()
    position = State()

