from aiogram.dispatcher.filters.state import State, StatesGroup


class Speciality(StatesGroup):
    technique = State()
    pedagogy = State()
    economy = State()
    medicine = State()
