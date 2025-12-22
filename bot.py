from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import requests

# ================== CONFIG ==================
BOT_TOKEN = "8540660925:AAE9YKg-RPga_L5yrA_wkBrA7Sol2p41MzE"               # BotFather से मिला token
NUMVERIFY_API_KEY = "b75f9d6cc44a1e6af71246a18881e62f"  # numverify.com से API key
# ============================================


# ---------- /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "📱 Mobile Number Information Bot\n\n"
        "👉 10 digit mobile number bhejo\n"
        "Example: 9812345678\n\n"
        "🔒 Educational purpose only"
    )


# ---------- Number Info Handler ----------
async def number_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Check valid 10 digit number
    if not text.isdigit() or len(text) != 10:
        await update.message.reply_text(
            "⚠️ Galat format!\n"
            "Sirf 10 digit mobile number bhejo\n"
            "Example: 9812345678"
        )
        return

    # India number format
    number = "91" + text

    url = "https://api.numverify.com/api/validate"
    params = {
        "access_key": NUMVERIFY_API_KEY,
        "number": number
    }

    try:
        response = requests.get(url, params=params, timeout=10).json()
    except:
        await update.message.reply_text("❌ API error, baad me try karo")
        return

    if response.get("valid") is True:
        msg = (
            "📍 Number Information\n"
            "——————————————\n"
            f"📞 Number: +{response.get('international_format')}\n"
            f"🌍 Country: {response.get('country_name')}\n"
            f"📶 Operator: {response.get('carrier')}\n"
            f"📱 Line Type: {response.get('line_type')}\n\n"
            "✅ Valid Number"
        )
    else:
        msg = (
            "❌ Invalid Mobile Number\n\n"
            "Kripya sahi number bheje"
        )

    await update.message.reply_text(msg)


# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, number_info))

    print("🤖 Number Info Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()