import config
import asyncio

from pyrogram import filters

from FallenMusic import app, OWNER_ID


@app.on_message(filters.command("config", "variables") & filters.private & filters.user(OWNER_ID))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "**» ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\nɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴠᴀʀɪᴀʙʟᴇs...**"
    )
    text = f"""**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**

ᴀᴩɪ_ɪᴅ : `{config.API_ID}`
ᴀᴩɪ_ʜᴀsʜ : `{config.API_HASH}`
ᴀss_ʜᴀɴᴅʟᴇʀ : `{config.ASS_HANDLER}`
ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ : `{config.DURATION_LIMIT}`
ʟᴏɢɢᴇʀ_ɪᴅ : `{config.LOGGER_ID}`
ᴍᴏɴɢᴏ_ᴅʙ_ᴜʀɪ : `{config.MONGO_DB_URI}`
ᴏᴡɴᴇʀ_ɪᴅ : `{config.OWNER_ID}`
ᴩɪɴɢ_ɪᴍɢ : `{config.PING_IMG}`
sᴛᴀʀᴛ_ɪᴍɢ : `{config.START_IMG}`
sᴜᴩᴩᴏʀᴛ_ᴄʜᴀᴛ : `{config.SUPPORT_CHAT}`
sᴜᴩᴩᴏʀᴛ_ᴄʜᴀɴɴᴇʟ : `{config.SUPPORT_CHANNEL}`
sᴜᴅᴏ_ᴜsᴇʀs : `{config.SUDO_USERS}`

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
