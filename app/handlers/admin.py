from aiogram import Router, types
from aiogram.types import Message, CallbackQuery
import app.keyboards.inline as ikb
import app.keyboards.reply as rkb
from db import get_user_count, get_all_user_ids
from config import ADMINS

admin_router = Router()

broadcast_text = ""
broadcast_photo = ""

@admin_router.message(lambda msg: msg.text == 'адм')
async def admin_panel(message: Message):
    if message.from_user.id in ADMINS:
        await message.reply('👮‍♂️ Добро пожаловать в панель администратора', reply_markup=ikb.admin_panel)

@admin_router.callback_query(lambda cb: cb.data == 'get_users')
async def get_users_count(callback: CallbackQuery):
    count = get_user_count()
    await callback.answer(f'📊 Количество участников бота: {count}')

@admin_router.callback_query(lambda cb: cb.data == 'set_bc_text')
async def set_bc_text(callback: CallbackQuery):
    await callback.message.answer("Введите текст рассылки:")

@admin_router.callback_query(lambda cb: cb.data == 'set_bc_photo')
async def set_bc_photo(callback: CallbackQuery):
    await callback.message.answer("Отправьте фото для рассылки:")

@admin_router.message(lambda m: m.text)
async def receive_text(message: Message):
    global broadcast_text
    if message.from_user.id in ADMINS:
        broadcast_text = message.text
        await message.reply("✅ Текст рассылки установлен!")

@admin_router.message(lambda m: m.photo)
async def receive_photo(message: Message):
    global broadcast_photo
    if message.from_user.id in ADMINS:
        broadcast_photo = message.photo[-1].file_id
        await message.reply("✅ Фото рассылки установлено!")

@admin_router.callback_query(lambda cb: cb.data == 'say_broadcast')
async def send_broadcast(callback: CallbackQuery):
    users = get_all_user_ids()
    count = 0
    if not broadcast_text and not broadcast_photo:
        await callback.answer("Сначала задайте текст и фото для рассылки", show_alert=True)
        return
    for user_id in users:
        try:
            if broadcast_text and broadcast_photo:
                await callback.message.bot.send_photo(user_id, broadcast_photo, caption=broadcast_text)
            elif broadcast_text:
                await callback.message.bot.send_message(user_id, broadcast_text)
            elif broadcast_photo:
                await callback.message.bot.send_photo(user_id, broadcast_photo)
            count += 1
        except Exception as e:
            print(f"[!] Не удалось отправить пользователю {user_id}: {e}")

    await callback.answer(f'📢 Рассылка отправлена {count} пользователям')

@admin_router.callback_query(lambda cb: cb.data == 'clear_text')
async def clear_broadcast(callback: CallbackQuery):
    global broadcast_text, broadcast_photo
    broadcast_text = ""
    await callback.answer("🗑️ Текст очищен")
    await callback.message.edit_reply_markup(reply_markup=ikb.admin_panel)

@admin_router.callback_query(lambda cb: cb.data == 'clear_text')
async def clear_broadcast(callback: CallbackQuery):
    global broadcast_text, broadcast_photo
    broadcast_photo = ""
    await callback.answer("🗑️ Фото очищено")
    await callback.message.edit_reply_markup(reply_markup=ikb.admin_panel)

@admin_router.callback_query(lambda cb: cb.data == 'rassilka')
async def clear_broadcast(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=ikb.rassilka)

@admin_router.callback_query(lambda cb: cb.data == 'back_admin')
async def clear_broadcast(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=ikb.admin_panel)