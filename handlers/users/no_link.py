from aiogram import types

from loader import dp

NO_LINK_REGEX = "^[^.]*$"


@dp.message_handler(regexp=NO_LINK_REGEX)
async def bot_no_link(message: types.Message):
    await message.answer("I can't talk with humans, only process links 🤖")
