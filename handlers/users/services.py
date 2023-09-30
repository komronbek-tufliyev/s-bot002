from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from api import *
from keyboards.default.services_button import services, article_buttons
from states.services import Services


@dp.message_handler(Text(equals=['📝 Услуги', '📝 Xizmatlar', '📝 Services']))
async def services_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("Xizmatlarimiz", reply_markup=services(language))
    elif language == 'ru':
        await message.answer("Наши услуги", reply_markup=services(language))
    else:
        await message.answer("Our services", reply_markup=services(language))


@dp.message_handler(Text(equals=['Maqola', 'Статья', 'Article']))
async def article_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer(text="Quyidagilardan birini tanlang 👇", reply_markup=article_buttons(language))
    elif language == 'ru':
        await message.answer(text="Choose one of the following 👇", reply_markup=article_buttons(language))
    else:
        await message.answer(text="Выберите один из следующих 👇", reply_markup=article_buttons(language))
    # await state.finish()


@dp.message_handler(Text(equals=['DGU', 'Патент', 'Patent']))
async def patent_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("Bot test rejimida ishlamoqda. Iltimos, keyinroq urinib ko'ring!")
    elif language == 'ru':
        await message.answer("Бот работает в тестовом режиме. Пожалуйста, попробуйте позже!")
    else:
        await message.answer("The bot is working in test mode. Please try again later!")
    # await state.finish()


@dp.message_handler(Text(equals=['Sertifikat', 'Сертификат', 'Certificate']))
async def certificate_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("Bot test rejimida ishlamoqda. Iltimos, keyinroq urinib ko'ring!")
    elif language == 'ru':
        await message.answer("Бот работает в тестовом режиме. Пожалуйста, попробуйте позже!")
    else:
        await message.answer("The bot is working in test mode. Please try again later!")
    # await state.finish()




