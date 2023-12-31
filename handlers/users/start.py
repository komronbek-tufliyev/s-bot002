from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
# aiogram formatting
from aiogram.types import ParseMode

from loader import dp

from api import *
from states import Language
from keyboards.default.menus import *


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

# Bu funksiya botni ishga tushurishda ishlatiladi. Va foydalanuvchini bazaga qo'shadi.
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    telegram_id = message.from_user.id
    # print(full_name, username, telegram_id)
    # print(message.from_user.to_python())

    # ushbu funksiya api.py da yozilgan va foydalanuvchini bazada mavjud bo'lmasa, uni bazaga qo'shadi.
    check = create_user(telegram_id, message.from_user.to_python())
    # print(check)
    if check == 400:
        language = language_info(telegram_id)
        if language == 'uz':
            await message.answer("✅ Bosh menyuga xush kelibsiz\n"
                                 f"💻 Maqola, jurnal yozish, mahalliy va xalqaro jurnallarda chop etish xizmatlari! "
                                 f"Buyurtma berishni boshlaysizmi?",
                                 reply_markup=main_uz, parse_mode=ParseMode.HTML)
        elif language == 'ru':
            await message.answer("✅ Добро пожаловать в главное меню\n"
                                 f"💻 Статьи, написание журналов, издательские услуги в местных и международных "
                                 f"журналах! Вкусный пиццы! Вы начинайте заказывать?",
                                 reply_markup=main_ru)
        elif language == 'en':
            await message.answer("✅ Welcome to the main menu\n"
                                 f"💻 Articles, magazine writing, publishing services in local and international "
                                 f"magazines! Shall we start ordering?",
                                 reply_markup=main_en)
    else:
        await message.answer(f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"
                             f"🇷🇺 Для использования бота выберите удобный для вас язык.\n"
                             f"🇬🇧 Choose a convenient language for you to use the bot.",
                             reply_markup=choose_language)
        create_user(telegram_id, message.from_user.to_python())
        await Language.language.set()


# Bu funksiya foydalanuvchining tilini o'zgartirishda ishlatiladi. Qachonki foydalanuvchi botni ishga tushuradi,
# shunda ushbu funksiya ishga tushadi.
@dp.message_handler(state=Language.language)
async def set_language_system(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text in ['🇺🇿 O\'zbekcha', '🇷🇺 Русский', '🇬🇧 English']:
            if message.text == '🇺🇿 O\'zbekcha':
                change_language(telegram_id=message.from_user.id, language='uz')
                await message.answer("✅ Bosh menyuga xush kelibsiz\n"
                                     f"💻 Maqola, jurnal yozish, mahalliy va xalqaro jurnallarda chop etish "
                                     f"xizmatlari! Buyurtma berishni boshlaysizmi?",
                                     reply_markup=main_uz)
            elif message.text == '🇷🇺 Русский':
                change_language(telegram_id=message.from_user.id, language='ru')
                await message.answer("✅ Добро пожаловать в главное меню\n"
                                     f"💻 Статьи, написание журналов, издательские услуги в местных и международных "
                                     f"журналах! Вы начинайте заказывать?",
                                     reply_markup=main_ru)
            elif message.text == '🇬🇧 English':
                change_language(telegram_id=message.from_user.id, language='en')
                await message.answer("✅ Welcome to the main menu\n"
                                     f"💻 Articles, magazine writing, publishing services in local and international "
                                     f"magazines! Shall we start ordering?",
                                     reply_markup=main_en)
            await state.finish()
        else:
            await message.answer(" 🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"
                                 " 🇷🇺 Для использования бота выберите удобный для вас язык.\n"
                                 " 🇬🇧 Choose a convenient language for you to use the bot.",
                                 reply_markup=choose_language)
            await Language.language.set()
    else:
        await message.answer(" 🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"
                             " 🇷🇺 Для использования бота выберите удобный для вас язык.\n"
                             " 🇬🇧 Choose a convenient language for you to use the bot.",
                             reply_markup=choose_language)
        await Language.language.set()
