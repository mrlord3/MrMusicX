import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","لورد","السورس", "سورس لورد"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ba49699e0baee040f3737.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  𝐒𝐎𝐔𝐑𝐂𝐄 𝐋𝐎𝐑𝐃(t.me/M_R_ZC)
么 [َ 𝙳𝙴𝚅 𝙻𝙾𝚁𝙳 ](t.me/M_R_C2)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/N3_NG)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  𝙳𝙴𝚅 𝙻𝙾𝚁𝙳 . 🕷 › ", url=f"https://t.me/M_R_C2"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/M_R_ZC"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/N3_NG"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
