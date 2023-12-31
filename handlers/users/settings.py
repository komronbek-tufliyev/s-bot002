import logging
from loader import dp, bot
from aiogram import types
from api import *
from keyboards.default.menus import *
from keyboards.default.services_button import *
from keyboards.default.settings_button import *
from aiogram.dispatcher import FSMContext

from states import Language


# ###########  Settings Button ############## #
@dp.message_handler(text=["⚙️ Настройки", "⚙️ Sozlamalar", "⚙️ Settings"])
async def gotosettings(message: types.Message):
    """
    This function is used to go to the settings section.
    And it is used in the main menu.
    """
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("⚙️ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧  Tugmachalar orqali tilni o'zgartirishingiz mumkin.",
                             reply_markup=settings(language))

    elif language == 'en':
        await message.answer("⚙️ Welcome to settings!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧 You can change the language using the buttons.",
                             reply_markup=settings(language))

    else:
        await message.answer("⚙️ Добро пожаловать в настройки!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))


# ##########  Select Language  ############## #
@dp.message_handler(text=["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
async def change_lang(message: types.Message):
    """
    This function is used to change the language of the user.
    """
    if message.text == "🇺🇿 O'zbekcha":
        change_language(telegram_id=message.from_user.id, language="uz")
        await message.answer(
            f"🙂 Assalomu alaykum, {message.from_user.full_name}, @new_scientist_bot botiga xush kelibsiz!\n\n"
            "📚 Ushbu bot orqali mahalliy va xalqaro ilmiy jurnallardan "
            "siz yozgan maqola va boshqalarni chop etishingiz, ilmiy ishingiz uchun "
            "kerakli materiallar olishingiz mumkin. Marhamat xizmatlarimizidan foydalaning!\n\n"
            "💻 Buyurtna berishni boshlaysizmi?", reply_markup=main_uz)
    elif message.text == "🇬🇧 English":
        change_language(telegram_id=message.from_user.id, language="en")
        await message.answer(f"🙂 Hello, {message.from_user.full_name}, welcome to @new_scientist_bot!\n\n"
                             "📚 Through this bot, you can publish your articles and "
                             "others from local and international scientific journals, "
                             "and get necessary materials for your scientific work. "
                             "Take advantage of our services!\n\n" 
                             "💻 Are you starting to order?", reply_markup=main_en)
    else:
        change_language(telegram_id=message.from_user.id, language="ru")
        await message.answer(
            f"🙂 Здравствуйте, {message.from_user.full_name}, добро пожаловать в бот @new_scientist_bot!\n\n"
            "📚 С помощью этого бота вы можете публиковать свои и "
            "другие статьи из местных и международных научных журналов, "
            "а также получать необходимые материалы для своей научной работы. "
            "Воспользуйтесь нашими услугами!\n\n"
            "💻 Начать заказывать?", reply_markup=main_ru)


# ###############  Go to Menu  ################# #
@dp.message_handler(text=["🔝 Bosh menyuga qaytish", "🔝 Вернуться в главное меню", "🔝 Return to main menu", "/menu"])
async def main_menu_handler(message: types.Message):
    """
        Agar foydalanuvchi bosh menyuga qaytishni istasa, ushbu funksiya ishlatiladi.
    """
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("✅ Bosh menyuga xush kelibsiz\n"
                             f"💻 Maqola, jurnal yozish, mahalliy va xalqaro jurnallarda "
                             f"chop etish xizmatlari! Buyurtma berishni boshlaysizmi?",
                             reply_markup=main_uz)
    elif language == 'en':
        await message.answer("✅ Welcome to the main menu\n"
                             f"💻 Articles, magazine writing, publishing services in local and "
                             f"international magazines! Are you starting to order?",
                             reply_markup=main_en)
    else:
        await message.answer("✅ Добро пожаловать в главное меню\n"
                             f"💻 Статьи, написание журналов, издательские услуги в местных и "
                             f"международных журналах! Вы начинайте заказывать?",
                             reply_markup=main_ru)


# # go back previous state (step)
# @dp.message_handler(text=["⬅️ Orqaga", "⬅️ Назад", "⬅️ Back"])
# async def back_handler(message:types.Message, state:FSMContext):
#     """
#         Agar foydalanuvchi oldingi qadimgi holatga qaytishni istasa,
#         ushbu funksiya ishlatiladi. Va oldingi stateda yuborilishi kerak bo'lgan handler chaqiriladi.
#     """
#     logging.info(f"State: {await state.get_state()}")
#     print(f"State: {await state.get_state()}")
#     # await Level.previous()
#     if await Level.previous():
#         if not Language.language:
#             print("No previous lang state")
#             await state.finish()

#         else:
#             await Language.language.set()
#         print("No previous state")
#     else:
#         await state.set_state(await Level.previous())
#     print(f"State after: {await state.get_state()}")
#     # await dp.current_state().reset_state(with_data=False)


# @dp.message_handler(text=["⬅️ Orqaga", "⬅️ Назад", "⬅️ Back"])
# async def back_handler(message: types.Message, state: FSMContext):
#     logging.info(f"State: {await state.get_state()}")

#     previous_state = await Level.previous()

#     if previous_state is not None:
#         logging.info("Going to the previous state")
#         if not Language.language:
#             print("No previous lang state")
#             await state.finish()
#         else:
#             logging.info("Setting Language:language state")
#             await Language.language.set()
#     else:
#         logging.info("No previous state found")
#         await state.finish()

#     print(f"State after: {await state.get_state()}")
#     # await dp.current_state().reset_state(with_data=False)


# #################  Change Language Command   ################ #
@dp.message_handler(commands='set_language')
async def change_language_handler(message: types.Message):
    """
        Bot tilini o'zgartirish uchun ishlatiladi. va /set_language
        commandasi orqali ishga tushiriladi.
    """

    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("⚙️ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧  Tugmachalar orqali tilni o'zgartirishingiz mumkin.",
                             reply_markup=settings(language))

    elif language == 'en':
        await message.answer("⚙️ Welcome to settings!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧 You can change the language using the buttons.",
                             reply_markup=settings(language))

    else:
        await message.answer("⚙️ Добро пожаловать в настройки!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))


# Get contact
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def get_contact(message: types.Message):
    """
        Botga yuborilgan contactni olish uchun ishlatiladi.
    """
    language = language_info(message.from_user.id)
    phone = message.contact.phone_number
    change_phone(telegram_id=message.from_user.id, phone=phone)

    if language == 'uz':
        await message.answer("📞 Telefon raqamingiz qabul qilindi. Rahmat!")
    elif language == 'en':
        await message.answer("📞 Your phone number has been received. Thank you!")
    else:
        await message.answer("📞 Ваш номер телефона получен. Спасибо!")