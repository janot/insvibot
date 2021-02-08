# Insvibot

Telegram bot for hiding Instant View links.

![](https://telegra.ph/file/d10f83f11654666bb3ebc.png)

## How does it work?

To create Instant View for your site, you must use [long link](https://instantview.telegram.org/) such as `https://t.me/iv?url=https%3A%2F%2Fnachasi.com%2F2020%2F04%2F24%2Fna-chasi-3-roky%2F&rhash=cc666c3caa4dd4`.

And as you can see, it is ugly.

[Insvibot](https://t.me/insvibot) fixes that by hiding `t.me/iv` link into non-breaking space.

After that you can copy bot's message and paste/forward it anywhere you want: to your channel, mom or even to Saved Messages.

## Installation and launch

1. Launch the [mongo database](https://www.mongodb.com/try/download/community) locally
2. Create and activate virtual environment:
    ```shell
    python -m venv venv
    source venv/bin/activate
    # venv\bin\activate.bat - for Windows
    ```
3. Install requirements:
   ```shell
    pip install -r requirements.txt
    ```
4. Rename file `.env.sample` to `.env` and change variables:
    - `ADMINS` - list of `user_id` of bot admins
    - `BOT_TOKEN` - Telegram bot token
5. Run `python app.py`

---

You can change logging options in `utils/misc/logging.py`

