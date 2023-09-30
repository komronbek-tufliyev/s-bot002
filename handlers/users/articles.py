from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import dp
from api import *
from keyboards.default.article_buttons import article_buttons_list, article_services, article_services_list


@dp.message_handler(Text(equals=article_buttons_list()))
async def article_categories_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer(text=f"Rahmat, {message.text}", reply_markup=article_services(language))
    elif language == 'ru':
        await message.answer(text=f"Спасибо {message.text}", reply_markup=article_services(language))
    else:
        await message.answer(text=f"Thank you {message.text}", reply_markup=article_services(language))


@dp.message_handler(Text(article_services_list()))
async def article_service_handler(message: types.Message, state: FSMContext):
    await message.answer(f"ashnaqade {message.text}")



