# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
import config


@Client.on_message(filters.command("panel"))
async def panel(_, message):

    if message.from_user.id != config.OWNER_ID:
        return

    text = """
🧠 ADMIN PANEL

Available Controls:

/stats - Bot statistics
/broadcast - Broadcast message
/batch - Batch page creator
"""

    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
