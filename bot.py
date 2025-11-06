import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8584981668:AAHm1RTtVp4nJ7TVxwG3pmfn9q--obqsSz0")
PUBLIC_URL = os.getenv("https://telegram-bot-r4az.onrender.com")
PORT = int(os.getenv("PORT", "10000"))

AUTO_REPLY = (
    "Теперь все запросы, которые вы раньше отправляли в группу «Конструкции РИМ / САЙТ», "
    "нужно передавать через заявку в Битрикс24.\n\n"
    "Почему это удобно:\n"
    "— Ответственные исполнители сразу видят поставленную задачу.\n"
    "— Вы видите ответы только по своим заявкам.\n"
    "— Можно отслеживать статус и сроки решения.\n\n"
    "Инструкция:\n"
    "• [Google Документ](https://docs.google.com/document/d/1CXJovq3JmKXqIvku1GOaV6gyg9SdPs23oaIg4iVUl9I/edit?tab=t.0)\n"
    "• [iSpring база знаний](https://rim-m.ispringlearn.ru/app/user-portal/knowledge-base/content-player/76ef7137-b3d6-11f0-af74-02756f8b0442)\n\n"
    "Если возникнут вопросы — напишите @MakarOsipov 🧡"
)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            AUTO_REPLY,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )

def main():
    if not TOKEN or not PUBLIC_URL:
        raise RuntimeError("Не заданы BOT_TOKEN или PUBLIC_URL")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, reply))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{PUBLIC_URL}/{TOKEN}",
    )

if __name__ == "__main__":
    main()
