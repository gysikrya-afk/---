import os
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from app.keyboard import yes_no,gender,number
from app.fsm_group import Opros

load_dotenv()
ID = os.getenv('ID_CHAT')

router = Router()

@router.message(F.text == '/start')
async def start(msg):
    await msg.answer('Привет.Хотите провести опрос?',reply_markup=yes_no)

@router.message(F.text == 'Нет')
async def no(msg):
    await msg.answer('Нет?Ладно...Это всё.Этот бот должен был быть для опроса.Тогда идите в начало что-бы начать опрос')

@router.message(F.text == 'Да')
async def opros_name(msg,state:FSMContext):
    await msg.answer('Начинаем опрос')
    await msg.answer('Как вас зовут:')
    await state.set_state(Opros.age)

@router.message(Opros.age)
async def opros_age(msg,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Сколько вам лет:')
    await state.set_state(Opros.gender)

@router.message(Opros.gender)
async def opros_gender(msg,state:FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer('Какого вы пола:',reply_markup=gender)
    await state.set_state(Opros.town)

@router.message(Opros.town)
async def opros_town(msg,state:FSMContext):
    await state.update_data(gender=msg.text)
    await msg.answer('Из какого вы города:')
    await state.set_state(Opros.number)

@router.message(Opros.number)
async def opros_number(msg,state:FSMContext):
    await state.update_data(town=msg.text)
    await msg.answer('Хотите ввести номер телефона?',reply_markup=number)
    await state.set_state(Opros.email)

@router.message(Opros.email)
async def opros_email(msg,state:FSMContext):
    await state.update_data(phone=msg.text)
    await msg.answer('Введите електронную почту:')
    await state.set_state(Opros.result)

@router.message(Opros.result)
async def result(msg,state:FSMContext):
    await state.update_data(email=msg.text)
    user_data = await state.get_data()
    name = user_data.get('name','Не указано')
    age = user_data.get('age','Не указано')
    gender = user_data.get('gender','Не указано')
    number = user_data.get('number','Не указано')
    email = user_data.get('email','Не указано')
    await msg.answer('Спасибо что приняли участвие в опросе.Мы вам благодарны!')
    await msg.bot.send_message(
        ID,f'Пришло сообщение от пользователя.\nИмя:{name}\nВозраст:{age}\nПол:{gender}\nНомер телефона:{number}\nЕлектронная почта:{email}')
