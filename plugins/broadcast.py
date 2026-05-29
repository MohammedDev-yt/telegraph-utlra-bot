# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from database import users
import config


@Client.on_message(filters.command("broadcast"))
async def broadcast(client, message):

    if message.from_user.id != config.OWNER_ID:
        return

    if not message.reply_to_message:

        return await message.reply_text(
            "Reply to a message"
        )

    text = (
        message.reply_to_message.text
        or message.reply_to_message.caption
    )

    sent = 0

    for user in users.find():

        try:

            await client.send_message(
                user["user_id"],
                text
            )

            sent += 1

        except:
            pass

    await message.reply_text(
        f"📢 Broadcast Sent To {sent} Users"
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
