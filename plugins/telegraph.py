# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegraph import Telegraph
from database import save_post

tg = Telegraph()

tg.create_account(short_name="ultra-bot")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def html_format(text):
    return text.replace("\n", "<br>")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def create_page(title, content):
    response = tg.create_page(
        title=title,
        html_content=content
    )

    return response["url"]


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- CREATE PAGE ---------------- #
@Client.on_message(filters.command("tgm"))
async def telegraph(_, message):

    title = "Telegraph Post"

    text = None

    # /tgm title | text
    if "|" in message.text:

        try:
            title, text = message.text.split("|", 1)

            title = title.split(None, 1)[1].strip()

            text = text.strip()

        except:
            pass

    # reply support
    elif message.reply_to_message:

        text = (
            message.reply_to_message.text
            or message.reply_to_message.caption
        )

    # direct text
    elif len(message.command) > 1:

        text = message.text.split(None, 1)[1]

    if not text:

        return await message.reply_text(
            "❌ Send some text"
        )

    url = create_page(
        title,
        html_format(text)
    )

    save_post(
        message.from_user.id,
        url,
        title
    )

    await message.reply_text(
        f"✅ Telegraph Created\n\n{url}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌐 Open",
                        url=url
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- IMAGE UPLOAD ---------------- #
@Client.on_message(filters.photo)
async def upload_photo(_, message):

    file_path = await message.download()

    try:

        response = tg.upload_file(file_path)

        telegraph_url = (
            "https://telegra.ph" + response[0]
        )

        os.remove(file_path)

        await message.reply_text(
            f"🖼 Uploaded To Telegraph\n\n{telegraph_url}"
        )

    except Exception as e:

        await message.reply_text(str(e))

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
