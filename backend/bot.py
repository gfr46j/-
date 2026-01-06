import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from dotenv import load_dotenv
load_dotenv()


TOKEN = os.environ['TELEGRAM_TOKEN']
NEWS_SOURCES = {
    "Dotesports": "https://dotesports.com/feed",
    "EsportsInsider": "https://esportsinsider.com/feed",
    "CybersportUA": "https://cybersport.ua/feed",
}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт 👋!\n"
        "Я - демонстраційний бот магазину для МАН 2025-2026. 📰\n\n"
        "Напиши /help щоб побачити список команд."
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Доступні команди:\n\n"
        "/start - запустити бота\n"
        "/help - список команд\n"
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("✅ Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
