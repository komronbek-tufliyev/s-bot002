from aiogram import types
from api import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def services(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton(text='Maqola'))\
            .add(KeyboardButton(text='DGU'))\
            .add(KeyboardButton(text='Sertifikat'))\
            .add(KeyboardButton(text="⬅️ Orqaga"))
    elif language == 'ru':
        button.add(KeyboardButton(text='Статья'))\
            .add(KeyboardButton(text='Патент'))\
            .add(KeyboardButton(text='Сертификат'))\
            .add(KeyboardButton(text='⬅️ Назад'))
    else:
        button.add(KeyboardButton(text='Article'))\
            .add(KeyboardButton(text='Patent'))\
            .add(KeyboardButton(text='Certificate'))\
            .add(KeyboardButton(text='⬅️ Back'))

    return button

