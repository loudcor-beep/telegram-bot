from telegram.ext import Updater, MessageHandler, Filters

# 🔑 Вставь сюда свой токен от BotFather
TOKEN = "8584981668:AAHm1RTtVp4nJ7TVxwG3pmfn9q--obqsSz0"

# ✉️ Сообщение, которое бот будет отправлять
AUTO_REPLY = 'Все заявки из этого чата необходимо отправлять в Битрикс24 через раздел "Автоматизация"'

def reply(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=AUTO_REPLY)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
