from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю!")

app = Application.builder().token("8254883837:AAH3OrBHnfV4Rqu2XoASeHkBvcRD3aAZWPc").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

