```python
import os
import logging
import uuid
import shortuuid
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import requests

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

scheduler = AsyncIOScheduler()

async def task_journalière():
    logging.info("📨 Tâche automatique exécutée")

def generer_id_unique():
    return shortuuid.uuid()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name or "utilisateur"
    await update.message.reply_text(
        f"👋 Bonjour {user}, bienvenue sur YMB V.2!\n"
        f"Votre identifiant unique: {generer_id_unique()}"
)

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n/aide\n... (autres commandes)"
)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    await update.message.reply_text(f"🤖 Tu as dit: {text}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    scheduler.add_job(task_journalière, CronTrigger(hour="8", minute="00"))
    scheduler.start()

    logging.info("✅ Bot YMB V.2 lancé")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
```
