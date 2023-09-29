from aiogram.dispatcher.filters.state import State, StatesGroup


class Services(StatesGroup):
    article = State()
    patent = State()
    certificate = State()
