from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰE TO YOᑌᖇ GᖇOᑌᑭ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𖤍 الأوامر 𖤍", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="ᗰᖇ ᒪOᖇᗪ", url=f"https://t.me/M_R_C2"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰE TO YOᑌᖇ GᖇOᑌᑭ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𖤍 الأوامر 𖤍", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="ᗰᖇ ᒪOᖇᗪ", url=f"https://t.me/M_R_C2"),
        ],
    ]
    return buttons
