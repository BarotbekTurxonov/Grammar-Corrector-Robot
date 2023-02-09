from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from states.check import CheckState
# from data.gingerit import GingerIt
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state : FSMContext):
	await message.answer(f"Hello, {message.from_user.full_name}.Improve your english with me!\n\n<b>How to use :    <code>/check something get wrong!!</code></b>")
	await state.finish()





