from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from api import *


# Language buttons
choose_language = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
choose_language.insert(KeyboardButton('🇺🇿 O\'zbekcha')).insert(KeyboardButton('🇷🇺 Русский')).insert(KeyboardButton('🇬🇧 English'))

# Main menu buttons
main_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_uz.insert(KeyboardButton(text="📝 Xizmatlar")).row(KeyboardButton(text="🛒 Savat"), KeyboardButton(text="⚙️ Sozlamalar")).insert(KeyboardButton(text="✍️ Aloqa"))
main_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_ru.insert(KeyboardButton(text="📝 Услуги")).row(KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="⚙️ Настройки")).insert(KeyboardButton(text="✍️ Контакт"))
main_en = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_en.insert(KeyboardButton(text="📝 Services")).row(KeyboardButton(text="🛒 Basket"), KeyboardButton(text="⚙️ Settings")).insert(KeyboardButton(text="✍️ Contact"))


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


