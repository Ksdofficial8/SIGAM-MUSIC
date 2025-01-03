from pyrogram.types import InlineKeyboardButton
import asyncio
from pyrogram import Client, filters as pyrofl
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters

import config
from SHUKLAMUSIC import app


CBUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/RIYA_CHAT_SUPPORT")
        ],
        [
            InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/riya_network"),
            InlineKeyboardButton("˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/ll_THUNDER_lll")
        ],
        [
            InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data="settings_back_helper")
        ]
    ]
)


# Define ABUTTON outside of the HELP_X string
ABUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data="settings_back_helper")
        ]
    ]
)

HELP_C = """```
⌬ ๏ ʟᴇᴛ's ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ```

**⌬ [˹ɴɪᴋᴋɪ ꭙ ᴍᴜsɪᴄ˼](https://t.me/sommusic7_bot) ɪs ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴍᴜsɪᴄ | ᴠɪᴅᴇᴏ sᴛꝛᴇᴀᴍɪɴɢ ʙᴏᴛ ᴏɴ ᴛᴇʟᴇɢꝛᴧᴍ ғᴏꝛ ʏᴏᴜꝛ ɢꝛᴏᴜᴘs ᴀɴᴅ ᴄʜᴧɴɴᴇʟ**
```\n⌬ ʙᴇsᴛ ғᴇᴀsɪʙɪʟɪᴛʏ ᴏɴ ᴛᴏᴘ  ?```

**␥ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ
␥ sᴜᴘᴘᴏʀᴛ ᴠ2.0 ᴀᴜᴅɪᴏ sᴍᴏᴏᴛʜ
␥ ɴᴏ ʏᴛ ɪᴘ ʙʟᴏᴄᴋ ɪssᴜᴇ
␥ ʙᴧsᴇᴅ ᴏɴ ɴᴇᴡ ᴠᴇꝛsɪᴏɴ ᴏғ ᴘʏꝛᴏ-ɢꝛᴧᴍ
␥ ɴᴏ ᴘꝛᴏᴍᴏᴛɪᴏɴᴧʟ ᴧᴅs | ʜɪɢʜ ᴜᴘ-ᴛɪᴍᴇ 
␥ ʜɪɢʜ ɪɴғꝛᴧsᴛꝛᴜᴄᴛᴜꝛᴇ sᴇꝛᴠᴇꝛ
␥ ꝛᴇ-ᴇᴅɪᴛᴇᴅ ᴄᴏꝛᴇ | ʜɪɢʜʟʏ ᴏᴘᴛɪᴍɪsᴇ
␥ ɴᴏ ᴍᴏꝛᴇ ʟᴧɢ ᴀɴᴅ ᴅᴏᴡɴ-ᴛɪᴍᴇ
␥ ᴍᴀɴʏ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs........

ᴀʟʟ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ

⌬ ᴍᴏʀᴇ ɪɴғᴏ. [ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ](https://t.me/RIYA_NETWORK)**"""

HELP_X = """```
    【◖ 𝐓ʜᴜɴᴅᴇʀ ◗ 】 🇮🇳 ᴍᴇɴᴜ```
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /**
␥ /play - Pʟᴀʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢ [ᴀᴜɪᴅᴏ].

␥ /vplay - Pʟᴀʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢ [ᴠɪᴅᴇᴏ].

␥ /pause - Sᴛᴏᴘ sᴏɴɢ[ᴀᴜɪᴅᴏ & ᴠɪᴅᴇᴏ].

␥ /resume - Cᴏɴᴛɪɴᴜᴇ ᴘʟᴀʏ sᴏɴɢ [ᴀᴜɪᴅᴏ & ᴠɪᴅᴇᴏ]

␥ /skip - Sᴋɪᴘ sᴏɴɢ [ᴀᴜɪᴅᴏ & ᴠɪᴅᴇᴏ]

␥ /end - Cʟᴇᴀʀ , ᴇɴᴅ ᴀʟʟ sᴏɴɢ [ᴀᴜɪᴅᴏ & ᴠɪᴅᴇᴏ]

V ɪ s ɪ ᴛ - [ʜᴇʀᴇ](https://t.me/RIYA_NETWORK)"""

# Callback query handler
@app.on_callback_query(filters.regex("ISTKHAR_ALAM"))
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(HELP_X, reply_markup=ABUTTON)

@app.on_callback_query(filters.regex("MUSARRAT"))
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(HELP_C, reply_markup=CBUTTON)

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            [InlineKeyboardButton(text=_["S_B_6"], callback_data="ISTKHAR_ALAM")],
            [InlineKeyboardButton(text=_["S_B_2"], callback_data="MUSARRAT")],
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons
