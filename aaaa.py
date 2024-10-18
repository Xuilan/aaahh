import logging
from uuid import uuid4
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Задаем уровень логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Получите ваш токен у BotFather и вставьте сюда
TELEGRAM_TOKEN = '7811609528:AAHFTVXPIQ_MgtH8gj2dwVR5s7T9KKcqsu0'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Idx Work /generate")

async def generate_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Генерируем уникальный идентификатор
    unique_id = str(uuid4())
    # Создаем уникальную ссылку
    link = f"https://cu94397.tw1.ru/generate/{unique_id}"
    await update.message.reply_text(f"Вот ваша уникальная ссылка: {link}")

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Добавление обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generate_link))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())