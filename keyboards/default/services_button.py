from aiogram import types
from api import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def services(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton(text='Maqola')) \
            .add(KeyboardButton(text='DGU')) \
            .add(KeyboardButton(text='Sertifikat')) \
            .add(KeyboardButton(text="⬅️ Orqaga"))
    elif language == 'ru':
        button.add(KeyboardButton(text='Статья')) \
            .add(KeyboardButton(text='Патент')) \
            .add(KeyboardButton(text='Сертификат')) \
            .add(KeyboardButton(text='⬅️ Назад'))
    else:
        button.add(KeyboardButton(text='Article')) \
            .add(KeyboardButton(text='Patent')) \
            .add(KeyboardButton(text='Certificate')) \
            .add(KeyboardButton(text='⬅️ Back'))

    return button


def article_buttons(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.add(KeyboardButton('OAK uchun')) \
            .add(KeyboardButton('Respublika konferensiya uchun')) \
            .add(KeyboardButton('Xalqaro konferensiya uchun')) \
            .add(KeyboardButton('Xalqaro ilmiy jurnal uchun')) \
            .add(KeyboardButton('⬅️ Orqaga'))
    elif language == 'ru':
        button.add(KeyboardButton('Для ОАК')) \
            .add(KeyboardButton('Для Республиканской конференции')) \
            .add(KeyboardButton('Для Международной конференции')) \
            .add(KeyboardButton('Для Международного научного журнала')) \
            .add(KeyboardButton('⬅️ Назад'))
    else:
        button.add(KeyboardButton('For OAK')) \
            .add(KeyboardButton('For Republic conference')) \
            .add(KeyboardButton('For International conference')) \
            .add(KeyboardButton('For International scientific journal')) \
            .add(KeyboardButton('⬅️ Back'))

    return button


def patent_buttons(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.add(KeyboardButton('OAK uchun')) \
            .add(KeyboardButton('Respublika konferensiya uchun')) \
            .add(KeyboardButton('Xalqaro konferensiya uchun')) \
            .add(KeyboardButton('Xalqaro ilmiy jurnal uchun')) \
            .add(KeyboardButton('⬅️ Orqaga'))
    elif language == 'ru':
        button.add(KeyboardButton('Для ОАК')) \
            .add(KeyboardButton('Для Республиканской конференции')) \
            .add(KeyboardButton('Для Международной конференции')) \
            .add(KeyboardButton('Для Международного научного журнала')) \
            .add(KeyboardButton('⬅️ Назад'))
    else:
        button.add(KeyboardButton('For OAK')) \
            .add(KeyboardButton('For Republic conference')) \
            .add(KeyboardButton('For International conference')) \
            .add(KeyboardButton('For International scientific journal')) \
            .add(KeyboardButton('⬅️ Back'))

    return button
