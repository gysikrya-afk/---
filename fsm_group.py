from aiogram.fsm.state import State,StatesGroup

class Opros(StatesGroup):
    name = State()
    age = State()
    gender = State()
    town = State()
    number = State()
    email = State()
    result = State()
