from os import getenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}! Welcome to my bot!")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot is running.")
    application.run_polling()


if __name__ == "__main__":
    main()