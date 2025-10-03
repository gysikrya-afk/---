from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Да')],
        [KeyboardButton(text='Нет')],
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
