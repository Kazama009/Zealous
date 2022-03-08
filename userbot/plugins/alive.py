import time

from datetime import datetime
from telethon import version
from platform import python_version

from userbot import client, StartTime, zelous_version
from ..Helpers.utils.events import reply_id
from ..Helpers.utils.utils import get_readable_time
from ..SQL.globals import gvarstatus
from ..Core.managers import edit_or_reply

plugin_category = "utils"

@client.cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info=
    {
        "header":"Check Zealous Status",
        "options": "You can set a pic by setting the media link in the ALIVE_PIC",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def alive(event):
    reply_to = await reply_id(event)
    uptime = get_readable_time((time.time() - StartTime))
    time = datetime.now()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**✮ MY BOT IS RUNNING SUCCESSFULLY ✮**"
    msg = await edit_or_reply("`Loading`")
    end = datetime.now()
    ping = (end - time).microseconds / 1000
    cap = gvarstatus("ALIVE_TEMPLATE") or temp
    text = cap.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        TIME=uptime,
        PY=python_version,
        TELE=version,
        VER=zelous_version,
        PING=ping
    )

    await edit_or_reply(
        text
    )

temp = """{ALIVE_TEXT}
**{EMOJI} Uptime:** `{TIME}`
**{EMOJI} Python Version :** `{PY}`
**{EMOJI} Telethon Version:** `{TELE}`
**{EMOJI} Zealous Version:** `{VER}`
**{EMOJI} Ping:** `{PING}`
"""