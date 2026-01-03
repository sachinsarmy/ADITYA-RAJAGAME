import os
from telegram import Update
from telegram.ext import Application, ContextTypes

try:
    from telegram.ext import ChatJoinRequestHandler
except ImportError:
    raise ImportError("ChatJoinRequestHandler is only available in python-telegram-bot v20+. Please upgrade your library.")

# Use direct file paths instead of folders for Railway compatibility
FILE_PATH = "files\\BHARAT CLUB NUMBER HACK PENAL (A1).apk"
VOICE_PATH = "voices\\RAVIVOICEHACK.ogg"

async def approve_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = getattr(update, "chat_join_request", None)
    if request is None:
        return  # Ignore updates that are not join requests

    user = request.from_user

    # Approve the user
    await request.approve()

    # Build welcome message with username
    welcome_message = f"""
👋🏻 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {user.mention_html()} 𝐁𝐑𝐎𝐓𝐇𝐄𝐑
 𝐓𝐎 𝗢𝗨𝗥 - 𝐁𝐇𝐀𝐑𝐀𝐓 𝐂𝐋𝐔𝐁  𝐏𝐑𝐈𝐕𝐀𝐓𝐄  𝐇𝐀𝐂𝐊 𝐒𝐄𝐑𝐕𝐄𝐑 🤑💵
  
    """

    # Send welcome message
    await context.bot.send_message(chat_id=user.id, text=welcome_message, parse_mode="HTML")

    # Send file
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "rb") as f:
            await context.bot.send_document(chat_id=user.id, document=f, caption="""
📂 ☆𝟏𝟎𝟎% 𝐍𝐔𝐌𝐁𝐄𝐑 𝐇𝐀𝐂𝐊💸

(𝐎𝐍𝐋𝐘 𝐅𝐎𝐑 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑𝐒)💎

(𝟏𝟎𝟎% 𝐋𝐎𝐒𝐒 𝐑𝐄𝐂𝐎𝐕𝐄𝐑 𝐆𝐔𝐀𝐑𝐀𝐍𝐓𝐄𝐄)🧬


♻𝐅𝐎𝐑 𝐇𝐄𝐋𝐏 @KING_GOD009

🔴𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐇𝐀𝐂𝐊💱
https://t.me/hack_vide

☆ 🚀""")
    else:
        await context.bot.send_message(chat_id=user.id, text="Sorry, the requested file is not available.")

    # Send voice message (if available)
    if os.path.exists(VOICE_PATH):
        with open(VOICE_PATH, "rb") as v:
            await context.bot.send_voice(chat_id=user.id, voice=v, caption="""
🎙 𝐌𝐄𝐌𝐁𝐄𝐑 𝟗𝐗 𝐏𝐑𝐎𝐅𝐈𝐓 𝐏𝐑𝐎𝐎𝐅 👇🏻 -

https://t.me/DIUWINSTARBOYBOT/6

𝐀𝐋𝐖𝐀𝐘𝐒 𝐁𝐀𝐂𝐊 𝐓𝐎 𝐁𝐀𝐂𝐊 𝐍𝐔𝐌𝐁𝐄𝐑 𝐖𝐈𝐍 🤑♻👑
""")
    else:
        await context.bot.send_message(chat_id=user.id, text="Sorry, the requested voice message is not available.")

def main():
    app = Application.builder().token("8455931318:AAGMZ1xRIqchet-24ujbeUW-Mg3CiCXZjO8").build()
    app.add_handler(ChatJoinRequestHandler(approve_and_send))
    app.run_polling()

if __name__ == "__main__":
    main()