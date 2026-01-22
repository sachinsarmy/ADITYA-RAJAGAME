import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    ChatJoinRequestHandler,
)

# ================= HARD CODED TOKEN =================
BOT_TOKEN = "7539536706:AAHk4mgyqv7AHw9tWHqA7K_5d1qNOgFXPQ8"
# ====================================================

APK_PATH = "𝐇ɪᴍᴀɴꜱʜᴜ_𝐍ᴜᴍʙᴇʀ_𝐇ᴀᴄᴋ_1.apk"
VOICE_PATH = "VOICEHACK.ogg"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def approve_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request
    if not request:
        return

    user = request.from_user
    chat_id = request.chat.id

    # ❌ AUTO APPROVE DISABLED
    # await context.bot.approve_chat_join_request(
    #     chat_id=chat_id,
    #     user_id=user.id
    # )

    # ---------- GREETING DM ----------
    welcome_message = f"""
👋🏻 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {user.mention_html()} 𝐁𝐑𝐎𝐓𝐇𝐄𝐑
𝐓𝐎 𝗢𝗨𝗥 - 𝐑𝐀𝐉𝐀 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐇𝐀𝐂𝐊 𝐒𝐄𝐑𝐕𝐄𝐑 🤑💵
"""

    await context.bot.send_message(
        chat_id=user.id,
        text=welcome_message,
        parse_mode="HTML",
    )

    # ---------- SEND APK ----------
    if os.path.exists(APK_PATH):
        with open(APK_PATH, "rb") as apk:
            await context.bot.send_document(
                chat_id=user.id,
                document=apk,
                caption="""
📂 ☆𝟏𝟎𝟎% 𝐍𝐔𝐌𝐁𝐄𝐑 𝐇𝐀𝐂𝐊💸

(केवल प्रीमियम उपयोगकर्ताओं के लिए)💎
(𝟏𝟎𝟎% नुकसान की भरपाई की गारंटी)🧬

♻सहायता के लिए @himanshu_972

🔴हैक का उपयोग कैसे करें
https://t.me/+vBKqhKW2V6BhMGU1
"""
            )

    # ---------- SEND VOICE ----------
    if os.path.exists(VOICE_PATH):
        with open(VOICE_PATH, "rb") as voice:
            await context.bot.send_voice(
                chat_id=user.id,
                voice=voice,
                caption="""
🎙 सदस्य 9X गुना लाभ का प्रमाण 👇🏻
https://t.me/rajaindiaprediction/54

लगातार नंबर पे नंबर जीतना 🤑♻👑
"""
            )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_and_send))

    # ✅ JOIN REQUEST UPDATES ONLY
    app.run_polling(allowed_updates=["chat_join_request"])

if __name__ == "__main__":
    main()


