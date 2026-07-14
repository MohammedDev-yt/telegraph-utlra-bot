# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import Telegraph
from database import save_post

# ---------------- TELEGRAPH INIT ---------------- #

tg = Telegraph()

try:
    tg.create_account(short_name="ultra-bot")
except:
    pass

# ---------------- HTML FORMAT ---------------- #

def html_format(text):
    if not text:
        return ""

    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br>")
    )

# ---------------- CREATE PAGE ---------------- #

def create_page(title, content):
    response = tg.create_page(
        title=title,
        html_content=content
    )
    return response["url"]

# ---------------- CREATE /TGM ---------------- #

@Client.on_message(filters.command("tgm"))
async def telegraph(_, message):

    title = "Telegraph Post"
    text = None

    # /tgm Title | Text
    if "|" in message.text:
        try:
            title, text = message.text.split("|", 1)
            title = title.split(None, 1)[1].strip()
            text = text.strip()
        except:
            pass

    # Reply to text message
    elif message.reply_to_message:
        reply = message.reply_to_message
        text = reply.text or reply.caption

    # Direct text
    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    # Validation
    if not text:
        return await message.reply_text(
            "❌ Send some text or reply to a text message"
        )

    # ---------------- BUILD CONTENT ---------------- #

    content = f"<p>{html_format(text)}</p>"

    # ---------------- FOOTER ---------------- #

    content += """
    <hr>
    <p><b>ᴄʜᴀɴɴᴇʟ :</b> <a href="https://t.me/Aero_Unity">ᴀᴇʀᴏ ᴜɴɪᴛʏ</a></p>
    <p><b>ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href="https://t.me/Mr_Mohammed_29">ᴍᴏʜᴀᴍᴍᴇᴅ</a></p>
    """

    # ---------------- CREATE PAGE ---------------- #

    url = create_page(title, content)

    save_post(message.from_user.id, url, title)

    await message.reply_text(
        f"✅ Telegraph Created\n\n{url}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• Open •", url=url)]]
        )
    )

# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #
