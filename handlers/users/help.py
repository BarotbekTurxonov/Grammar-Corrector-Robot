from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/info - Server haqida ma'lumot beradi",
            "/online - Barcha o'yinchilar ro'yxatini ko'rsatadi")
    
    await message.answer("\n".join(text))
