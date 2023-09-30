from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def article_buttons_list() -> list:
    return [
        'OAK uchun', 'Respublika konferensiya uchun',
        'Xalqaro konferensiya uchun', 'Xalqaro ilmiy jurnal uchun',
        'Для ОАК', 'Для Республиканской конференции',
        'Для Международного научного журнала', 'For OAK',
        'For Republic conference', 'For International conference',
        'For International scientific journal'
    ]


def article_services(language):
    button = ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
    if language == 'uz':
        button.add(KeyboardButton(text='Yozib berish')) \
            .add(KeyboardButton(text='Tayyor maqolani chop etish')) \
            .add(KeyboardButton(text='Yozib berish va chop etish')) \
            .add(KeyboardButton(text='⬅️ Orqaga')
                 )
    elif language == 'ru':
        button.add(KeyboardButton(text='Написать')) \
            .add(KeyboardButton(text='Распечатать готовую статью')) \
            .add(KeyboardButton(text='Написать и распечатать')) \
            .add(KeyboardButton(text='⬅️ Назад')
                 )
    else:
        button.add(KeyboardButton(text='Write')) \
            .add(KeyboardButton(text='Print a finished article')) \
            .add(KeyboardButton(text='Write and print')) \
            .add(KeyboardButton(text='⬅️ Back')
                 )

    return button


def article_services_list() -> list:
    return [
        'Yozib berish', 'Tayyor maqolani chop etish',
        'Yozib berish va chop etish', 'Написать',
        'Распечатать готовую статью', 'Написать и распечатать',
        'Write', 'Print a finished article', 'Write and print'
    ]
