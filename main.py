import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    ChatJoinRequestHandler,
)

# ================= CONFIG =================

BOT_TOKEN = os.getenv("8157438383:AAF2hzj6X0CJVDnYOLcR8YUYoUM0r0KKtl0")  # token from env (Git-safe)

APK_PATH = "DUIWIN AI SERVER PREDICTOR.apk"
VOICE_PATH = "VOICEHACK.ogg"

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")

# =========================================

logging.basicConfig(level=logging.INFO)

async def approve_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request
    if not request:
        return

    user = request.from_user

    # ✅ AUTO APPROVE (FIXED)
    await context.bot.approve_chat_join_request(
        chat_id=request.chat.id,
        user_id=user.id
    )

    # -------- GREETING DM --------
    welcome_message = f"""
👋🏻 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {user.mention_html()} 𝐁𝐑𝐎𝐓𝐇𝐄𝐑
𝐓𝐎 𝗢𝗨𝗥 - 𝐃𝐔𝐈𝐖𝐈𝐍 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐇𝐀𝐂𝐊 𝐒𝐄𝐑𝐕𝐄𝐑 🤑💵
"""

    await context.bot.send_message(
        chat_id=user.id,
        text=welcome_message,
        parse_mode="HTML"
    )

    # -------- SEND APK --------
    if os.path.exists(APK_PATH):
        with open(APK_PATH, "rb") as apk:
            await context.bot.send_document(
                chat_id=user.id,
                document=apk,
                caption="""
📂 ☆𝟏𝟎𝟎% 𝐍𝐔𝐌𝐁𝐄𝐑 𝐇𝐀𝐂𝐊💸

(𝐎𝐍𝐋𝐘 𝐅𝐎𝐑 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑𝐒)💎
(𝟏𝟎𝟎% 𝐋𝐎𝐒𝐒 𝐑𝐄𝐂𝐎𝐕𝐄𝐑 𝐆𝐔𝐀𝐑𝐀𝐍𝐓𝐄𝐄)🧬

♻𝐅𝐎𝐑 𝐇𝐄𝐋𝐏 @KING_GOD009

🔴𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄
https://t.me/hack_vide
"""
            )

    # -------- SEND VOICE --------
    if os.path.exists(VOICE_PATH):
        with open(VOICE_PATH, "rb") as voice:
            await context.bot.send_voice(
                chat_id=user.id,
                voice=voice,
                caption="""
🎙 𝐌𝐄𝐌𝐁𝐄𝐑 𝟗𝐗 𝐏𝐑𝐎𝐅𝐈𝐓 𝐏𝐑𝐎𝐎𝐅 👇🏻
https://t.me/DIUWINSTARBOYBOT/6

𝐀𝐋𝐖𝐀𝐘𝐒 𝐁𝐀𝐂𝐊 𝐓𝐎 𝐁𝐀𝐂𝐊 𝐍𝐔𝐌𝐁𝐄𝐑 𝐖𝐈𝐍 🤑♻👑
"""
            )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # ✅ JOIN REQUEST HANDLER
    app.add_handler(ChatJoinRequestHandler(approve_and_send))

    # ✅ IMPORTANT FIX (ensures join requests are received)
    app.run_polling(allowed_updates=["chat_join_request"])

if __name__ == "__main__":
    main()
