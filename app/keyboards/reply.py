from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1'), KeyboardButton(text='Кнопка 2'),
     KeyboardButton(text='Кнопка 3'), KeyboardButton(text='Кнопка 4')]
], resize_keyboard=True, input_field_placeholder='<3')

