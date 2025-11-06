from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 🔑 Вставь сюда токен, который дал BotFather
TOKEN = "8584981668:AAHm1RTtVp4nJ7TVxwG3pmfn9q--obqsSz0"

# ✉️ Сообщение, которое бот будет отправлять
AUTO_REPLY = 'Все заявки из этого чата необходимо отправлять в Битрикс24 через раздел "Автоматизация".'

# 🔄 Функция-обработчик входящих сообщений
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_REPLY)

# ⚙️ Настройка и запуск приложения
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("✅ Бот запущен и ждёт сообщения...")
app.run_polling()
