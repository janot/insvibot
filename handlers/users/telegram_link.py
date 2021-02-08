from aiogram import types
from aiogram.dispatcher import filters
from urllib.parse import urlsplit, parse_qs, unquote

from utils.database.api import add_domain

from loader import dp

IV_LINK_REGEX = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?t\.me(\/.*rhash=.*)$"
BROKEN_IV_LINK_REGEX = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?t\.me(\/*.*)$"


@dp.message_handler(filters.Regexp(regexp=IV_LINK_REGEX))
async def bot_link_telegram(message: types.Message):
    iv_link = unquote(message.text)
    iv_link_query = urlsplit(iv_link).query
    iv_link_params = parse_qs(iv_link_query)
    iv_link_params_dict = {param: value[0] for param, value in iv_link_params.items()}

    try:
        domain_name = iv_link_params_dict['url'].split("//")[-1].split("/")[0].replace('www.', '')
        rhash = iv_link_params_dict['rhash']

        add_domain(user_id=message.from_user.id, domain_name=domain_name, rhash=rhash)

        await message.answer(f"IV Link:\n"
                             f"{message.text}\n\n"
                             f"Domain: {domain_name}\n"
                             f"Rhash: {rhash}")

    # In case there is no url or rhash
    except KeyError:
        await message.answer("Your link seems broken.")


@dp.message_handler(filters.Regexp(regexp=BROKEN_IV_LINK_REGEX))
async def bot_broken_link_telegram(message: types.Message):
    await message.answer(f"Your link doesn't contain _rhash_:\n"
                         f"{message.text}", parse_mode="Markdown")
