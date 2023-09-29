from aiogram.dispatcher.filters.state import State, StatesGroup


class Articles(StatesGroup):
    type = State()
    service = ()
    client = ()

