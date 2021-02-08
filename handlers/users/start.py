from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.database.api import add_user, find_user

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not find_user(message.from_user.id):
        add_user(message.from_user.id)

    await message.answer('Send me "View in Telegram" link of <a href="https://instantview.telegram.org/my/">your Template</a>\nAfter this you can send me <b>regular</b> links and I\'ll convert them to IV\n\nНадішліть мені посилання "View in Telegram" <a href="https://instantview.telegram.org/my/">вашого Макету</a>\nПісля цього ви зможете надсилати мені <b>звичайні</b> посилання, а я додам IV до них', parse_mode="HTML")
