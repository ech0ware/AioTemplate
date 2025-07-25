from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inlinekb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Inline1', callback_data='inl1'), InlineKeyboardButton(text='Inline5', callback_data='inl5')],
    [InlineKeyboardButton(text='Inline2', callback_data='inl2'), InlineKeyboardButton(text='Inline6', callback_data='inl6')],
    [InlineKeyboardButton(text='Inline3', callback_data='inl3'), InlineKeyboardButton(text='Inline7', callback_data='inl7')],
    [InlineKeyboardButton(text='Inline4', callback_data='inl4'), InlineKeyboardButton(text='Inline8', callback_data='inl8')]
])

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📊 Статистика', callback_data='get_users')],
    [InlineKeyboardButton(text='📢 Рассылка', callback_data='rassilka')],
    [InlineKeyboardButton(text='✖️ Закрыть', callback_data='close')]
])

rassilka = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='📢 Запуск', callback_data='say_broadcast')],
[InlineKeyboardButton(text='📝 Установить текст', callback_data='set_bc_text')],
[InlineKeyboardButton(text='❌ Очистить текст', callback_data='clear_text')],
[InlineKeyboardButton(text='🖼 Фото рассылки', callback_data='set_bc_photo')],
[InlineKeyboardButton(text='❌ Очистить фото', callback_data='clear_photo')],
[InlineKeyboardButton(text='≡ В меню', callback_data='back_admin')],
])