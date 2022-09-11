import time
import config
import asyncio
from typing import Dict, List, Union

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)

from FallenMusic import ASSID, BOT_NAME, BOT_USERNAME, OWNER_ID, SUDO_USERS, app
from FallenMusic.Helpers.Database import (add_served_chat, add_served_user, blacklisted_chats, is_served_chat, remove_active_chat)
from FallenMusic.Cache.permission import PermissionCheck
from FallenMusic.Helpers.Inline import start_pannel


welcome_group = 2

__MODULE__ = "Sᴛᴀʀᴛ"
__HELP__ = """

/start 
» sᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ.

/help 
» sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʜᴇʟᴩ ᴍᴇɴᴜ ᴏғ ᴛʜᴇ ʙᴏᴛ.
"""


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    if chat_id in await blacklisted_chats():
        await message.reply_text(
            f"**» ᴡᴛғ**\n\nʏᴏᴜʀ ɢʀᴏᴜᴩ [{message.chat.title}] ɪs ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ.\n\nɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴜsᴇ ᴍᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ ᴀɴᴅ ʀᴇǫᴜᴇsᴛ ʜɪᴍ ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ ʏᴏᴜʀ ᴄʜᴀᴛ ᴇʟsᴇ ғᴜ*ᴋ ᴏғғ.\n\n**ᴠɪsɪᴛ :** [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ]({config.SUPPORT_CHAT})",
          disable_web_page_preview=True,
        )
        await app.leave_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id == ASSID:
                return await remove_active_chat(chat_id)
            if member.id in OWNER_ID:
                return await message.reply_text(
                    f"**» ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ {BOT_NAME} ᴊᴜsᴛ ᴊᴏɪɴᴇᴅ ʏᴏᴜʀ ᴄʜᴀᴛ.**\n\n➻ ᴏᴡɴᴇʀ : [{member.mention}] 🥀"
                )
            if member.id in SUDO_USERS:
                return await message.reply_text(
                    f"**» ᴀ sᴜᴅᴏ ᴜsᴇʀ ᴏғ {BOT_NAME} ᴊᴜsᴛ ᴊᴏɪɴᴇᴅ ʏᴏᴜʀ ᴄʜᴀᴛ.**\n\n➻ sᴜᴅᴏᴇʀ : [{member.mention}] 🥀"
                )
                return
        except:
            return


@app.on_message(filters.command(["help", "start", f"start@{BOT_USERNAME}"]) & filters.group)
@PermissionCheck
async def gstart(_, message: Message):
    out = start_pannel()
    await asyncio.gather(
        message.delete(),
        message.reply_text(
            f"» ʜᴇʏ,\nᴛʜɪs ɪs {BOT_NAME}\n ᴀ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.\n\nᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {message.chat.title}.\n\nɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪᴛ ɪɴ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ.",
            reply_markup=InlineKeyboardMarkup(out[1]),
        ),
    )
