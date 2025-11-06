from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8584981668:AAHm1RTtVp4nJ7TVxwG3pmfn9q--obqsSz0"
AUTO_REPLY = 'Все заявки из этого чата необходимо отправлять в Битрикс24 через раздел "Автоматизация"'

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_REPLY)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
