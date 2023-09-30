from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


# ############# Button Settings #############
def settings(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button.row(InlineKeyboardButton(text="🇺🇿 O'zbekcha"),
               InlineKeyboardButton(text="🇷🇺 Русский"),
               InlineKeyboardButton(text="🇬🇧 English"))
    if language == 'uz':
        # return to main menu
        button.insert(InlineKeyboardButton(text="🔝 Bosh menyuga qaytish")).insert(KeyboardButton(text="Kontaktni ulashish", request_contact=True),)
    elif language == 'en':
        # return to main menu
        button.row(InlineKeyboardButton(text="🔝 Return to main menu")).add(KeyboardButton(text="Share contact", request_contact=True),)
    else:
        button.row(InlineKeyboardButton(text="🔝 Вернуться в главное меню",)).add(KeyboardButton(text="Поделиться контактом", request_contact=True),)

    return button


# ############# Button Comment ############# #
def cancel(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Bekor qilish",))
    elif language == 'en':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Cancel",))
    else:
        button.row(InlineKeyboardButton(text="❌ Отменить",))

    return button
