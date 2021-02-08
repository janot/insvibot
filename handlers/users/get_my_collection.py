from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from utils.database.api import get_domain_list

from loader import dp


@dp.message_handler(Command(commands=["my", "domains", "list"]))
async def bot_my(message: types.Message):
    domain_list = get_domain_list(message.from_user.id)

    # Check if domain_list is empty
    if bool(domain_list):
        text = ("*List of your domains and rhashes:*\n",
                "\n".join("{}: `{}`".format(domain, rhash) for domain, rhash in domain_list.items()))
    else:
        text = ("You have no Templates yet.\n",
                "Try to make one on instantview.telegram.org")
    await message.answer("\n".join(text), parse_mode="Markdown")
