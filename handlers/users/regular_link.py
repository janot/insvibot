from aiogram import types
from aiogram.dispatcher import filters

from utils.database.api import get_rhash

from loader import dp

REGULAR_LINK_REGEX = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?(?!t\.me)([a-z0-9])+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"


@dp.message_handler(filters.Regexp(regexp=REGULAR_LINK_REGEX))
async def bot_link_format(message: types.Message):
    domain_name = message.text.split("//")[1].split("/")[0].replace('www.', '')
    rhash = get_rhash(user_id=message.from_user.id, domain_name=domain_name)
    if rhash:
        await message.answer(f"[⁠](https://t.me/iv?url={message.text}&rhash={rhash}){message.text}",
                             parse_mode="Markdown")
        await message.answer(f"[⁠](https://t.me/iv?url={message.text}&rhash={rhash})",
                             parse_mode="Markdown", disable_web_page_preview=True)
    else:
        await message.answer(f"You don't have Template for your domain {domain_name}")
