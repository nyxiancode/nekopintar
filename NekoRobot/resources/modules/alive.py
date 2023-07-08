import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from NekoRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from NekoRobot import telethn as tbot
from NekoRobot.events import register

PHOTO = [
    "https://telegra.ph/file/https://telegra.ph/file/6c19e38c494e4990a1223.jpg.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I am Neko Robot**\n\n➖➖➖➖➖➖➖➖➖➖➖\n\n"
    TEXT += f"» **My Developer : [Mogambo](https://t.me/{OWNER_USERNAME})**\n"
    TEXT += f"» **Library Version :** `{telever}` \n"
    TEXT += f"» **Telethon Version :** `{tlhver}` \n"
    TEXT += f"» **Pyrogram Version :** `{pyrover}` \n\n➖➖➖➖➖➖➖➖➖➖➖\n\n**Powered by @CyberMusicProject**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
