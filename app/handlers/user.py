from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards.inline as ikb
import app.keyboards.reply as rkb
from db import add_user_to_db

user_router = Router()
user_states = {}

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    add_user_to_db(user_id)
    await message.reply('Добро пожаловать в бота\n'
                        'Описание', parse_mode='HTML', reply_markup=ikb.inlinekb)


@user_router.message(lambda msg: msg.text == '123')
async def anon_mess(message: Message):
    await message.reply('Это пример текстового обработчика :D')

@user_router.callback_query(lambda cb: cb.data == 'inline')
async def clear_broadcast(callback: CallbackQuery):
    await callback.message.answer('Обработчик инлайн кнопки :D')

@user_router.message(lambda msg: msg.text == 'Я')
async def profile(message: Message):
    user = message.from_user
    # Вся инфа которую можно получить
    await message.reply(f'Юзернейм: {user.username}\n'
                        f'ID: {user.id}'
                        f'Никнейм: {user.full_name}\n'
                        f'Язык: {user.language_code}'
                        f'Телеграм премиум: {user.is_premium}\n'
                        f'')
