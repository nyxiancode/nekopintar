import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from NekoRobot import BOT_NAME, BOT_USERNAME
from NekoRobot import pbot as fallen


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "`Mohon tunggu...,\n\nMenulis teks Anda...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
Berhasil Menulis Teks 😼

**» Ditulis Oleh :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
**» Diminta oleh :** {message.from_user.mention}
**» Dukungan :** [Saluran Pembaruan](https://t.me/SayaNeko)
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "`Mohon tunggu...,\n\nMenulis teks Anda...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
Berhasil Menulis Teks 😼

**» Ditulis Oleh :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
**» Diminta oleh :** {message.from_user.mention}
**» Dukungan :** [SALURAN PEMBARUAN](https://t.me/SayaNeko)
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """

Menulis teks yang diberikan pada halaman putih dengan pena 🖊

» /write <teks> *:* Menulis teks yang diberikan.
"""
