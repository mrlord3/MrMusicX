import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
        ("الاوامر")
    ],
    
    [
        ("العكس"),
        ("احرف")
    ],
    [
        ("مطور السورس")
    ],
   
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار")
    ],
    [
        ("زخارف"),
        ("انصحني")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("احساب العمر")
    ],    

  
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

app.on_message(filters.regex("اخفاء الازرار . 🕷") & filters.group)
async def down(_, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب /start**", reply_markup= ReplyKeyboardRemove(selective=True))
    
@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/ba49699e0baee040f3737.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐋𝐎𝐑𝐃 𖠛", url=f"https://t.me/M_R_ZC"),
            ]
         ]
     )
  )

