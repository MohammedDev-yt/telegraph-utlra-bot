# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from telegraph import Telegraph
from database import save_batch

tg = Telegraph()

tg.create_account(short_name="batch-bot")


def create_page(title, content):

    response = tg.create_page(
        title=title,
        html_content=content
    )

    return response["url"]


@Client.on_message(filters.command("batch"))
async def batch(_, message):

    if "|" not in message.text:

        return await message.reply_text(
            "Usage:\n/batch Title | one,two,three"
        )

    title, texts = message.text.split("|", 1)

    title = title.split(None, 1)[1]

    urls = []

    for text in texts.split(","):

        url = create_page(
            title,
            text.strip()
        )

        urls.append(url)

    save_batch(
        message.from_user.id,
        urls
    )

    result = "\n".join(urls)

    await message.reply_text(
        f"✅ Batch Completed\n\n{result}"
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
