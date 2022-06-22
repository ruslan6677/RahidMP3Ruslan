from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAI8bmKIvgnlJyCrq9HIxSvCZCbm5CEjAAIaEAACpvFxHg-Z648-SCRWJAQ")
    await message.reply_text(
      f"""**[𝗟 Σ 𝗚 Σ 𝗡 𝗗](https://t.me/LegendMucisRobot) Sizi Salamlıyır👋🏻\n\nℹ️Mən Səsli Söhbətlərdə Musiqi Oxuya Bilən Bir Botam\n\n✅Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin**
      """,
         reply_markup
         =InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Məni öz qrubuna əlavə et ✅", url=f"https://t.me/LegendMucisRobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻Sahibim", url="https://t.me/o2o_GenCeLi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Kanal", url="https://t.me/SecretMMC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər" , callback_data= "cbhelp"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
      await message.reply_text(" Səsli söhbətdə Musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️\n\nMəsələn:\n\n1. `/play Ayaz Babayev - Sən Mənlə`\n2. `/play https://youtu.be/qLXUa89Q5WI`\n\n/alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız Bot sahibi istifadə edə bilər.\n\n⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "ℹ️ Bütün Əmirlərim", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "✅ Məlumatlarım", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "⬅️ Geri Qayıt", callback_data="cbstart")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" Səsli söhbətdə Musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️\n\nMəsələn:\n\n1. `/play Ayaz Babayev - Sən Mənlə`\n2. `/play https://youtu.be/qLXUa89Q5WI`\n\n/alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız Bot sahibi istifadə edə bilər.\n\n⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "ℹ️ Bütün Əmirlərim", callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "✅ Məlumatlarım",callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "⬅️ Geri Qayıt", callback_data="cbstart")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Hələ Hazır Deyiləm😁</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri Qayıt", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}! Bu botun hərkəs üçün əmr menyusu 😉\n\n/play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin.▶️\n/song  - İstədiyiniz musiqi sürətli bir şəkildə axtarın.🎵\n/vsong - İstədiyiniz videoları sürətli bir şəkildə axtarın.🔍\n\nBu botun adminlər üçün əmr menyusu ✅\n\n/pause - Musiqini dayandır.⏸️\n/resume - Musiqini dəvam etdir.▶️\n/end - Musiqini Bitir.⏹\n/skip - Musiqini keç.⏩\n/ses - Səsi 0-200 arasi dəyiş\n/reload - Botu yenidən başlad.🔄\n/asistan - Musiqi asistanı qrupunuza qoşulur.⚪\n\nSahiblər Və Sudo Üçün Əmirlər Menyusu\n\n/yetkiver - Yetki ver.🔼\n/yetkial - Yetki al.🔽\n/reklam - Bot Olduğu Butur Qrublarda Reklam Edər\n/restart - Botu Serverdən Yenidən Başlad\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "️⬅️ Geri Qayıt", callback_data="cbhelp")
                     ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**[𝗟 Σ 𝗚 Σ 𝗡 𝗗](https://t.me/LegendMucisRobot) Sizi Salamlıyır👋🏻\n\nℹ️Mən Səsli Söhbətlərdə Musiqi Oxuya Bilən Bir Botam\n\n✅Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Məni öz qrubuna əlavə et ✅", url=f"https://t.me/LegendMucisRobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻Sahibim", url="https://t.me/o2o_GenCeLi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Kanal", url="https://t.me/SecretMMC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər", callback_data= "cbhelp"
                    )
                ]
                
           ]
        ),
    )
