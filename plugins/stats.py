# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
from pyrogram import Client, filters
from database import (
    total_users,
    total_posts
)
import config

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("stats"))
async def stats(_, message):

    if message.from_user.id != config.OWNER_ID:
        return

    users = total_users()

    posts = total_posts()

    text = f"""
📊 Bot Statistics

👤 Total Users: {users}

📝 Total Posts: {posts}
"""

    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
