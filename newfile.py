from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8362894323:AAH0RpPmm4rfn7FrvZTmoB2cjybF7Rwbhsg"
CHANNEL_USERNAME = "@mr_monu_kacking"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            keyboard = [
                [InlineKeyboardButton("🔥 Feature 1", callback_data="f1")],
                [InlineKeyboardButton("⚙ Feature 2", callback_data="f2")],
                [InlineKeyboardButton("📺 YouTube Channel", url="https://youtube.com/@m.rhacker001?si=H-5iESLCOhKu5qjB")],
                [InlineKeyboardButton("👥 Telegram Group", url="https://t.me/+xKAPGp5S6qIyNWU1")]
            ]
            await update.message.reply_text(
                "✅ Welcome! अब आप bot का पूरा use कर सकते हैं 🚀",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            raise Exception("Not Joined")
    except:
        join_btn = InlineKeyboardButton(
            "Join Now ✅",
            url="https://t.me/mr_monu_kacking"
        )
        await update.message.reply_text(
            "🚫 Bot use करने से पहले हमारा channel join करें!\nJoin करने के बाद /start दबाएँ ✅",
            reply_markup=InlineKeyboardMarkup([[join_btn]])
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()