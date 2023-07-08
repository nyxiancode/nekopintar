from asyncio import sleep

from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights

from NekoRobot import DEMONS, DEV_USERS, DRAGONS, OWNER_ID, telethn

# =================== KONSTAN ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

OFFICERS = [OWNER_ID] + DEV_USERS + DRAGONS + DEMONS

# Periksa apakah pengguna memiliki hak admin


async def is_administrator(user_id: int, message):
    admin = False
    async for user in telethn.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or user_id in OFFICERS:
            admin = True
            break
    return admin


@telethn.on(events.NewMessage(pattern="^[!/]zombies ?(.*)"))
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**Grup bersih, tidak ditemukan akun yang dihapus.**"
    if con != "bersihkan":
        kontol = await show.reply("`Mencari akun yang dihapus untuk dihancurkan...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = (
                f"**Mencari...** `{del_u}` **Akun yang dihapus/Zombie pada grup ini,"
                "\nBersihkan dengan perintah** `/zombies bersihkan`"
            )
        return await kontol.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await show.reply("**Maaf, kamu bukan admin!**")
    memek = await show.reply("`Menghancurkan akun yang dihapus...`")
    del_u = 0
    del_a = 0
    async for user in telethn.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await show.edit("`Tidak memiliki hak untuk melarang di grup ini`")
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await telethn(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"**Dihancurkan** `{del_u}` **Zombie**"
    if del_a > 0:
        del_status = (
            f"**Dihancurkan** `{del_u}` **Zombie** "
            f"\n`{del_a}` **Admin zombie tidak dihapus.**"
        )
    await memek.edit(del_status)


__help__ = """
*Hapus Akun yang Dihapus*
» /zombies *:* Mulai mencari akun yang dihapus di dalam grup.
» /zombies bersihkan *:* Menghapus akun yang dihapus dari grup.
"""


__mod_name__ = "Zᴏᴍʙɪᴇ"
