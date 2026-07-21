from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8936188941:AAHbc_qrIfRLH_0NuUforvwzzdRYBnjRqh8"
ADMIN_ID = 8281892796

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "𝐒𝐩𝐞𝐚𝐤 𝐟𝐫𝐞𝐞𝐥𝐲.
𝐄𝐯𝐞𝐫𝐲 𝐰𝐨𝐫𝐝 𝐲𝐨𝐮 𝐥𝐞𝐚𝐯𝐞 𝐡𝐞𝐫𝐞 𝐫𝐞𝐦𝐚𝐢𝐧𝐬 𝐚 𝐬𝐞𝐜𝐫𝐞𝐭."
    )

async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    users[user.id] = user.id

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"پیام جدید از کاربر:\n\n{update.message.text}",
    )

async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        text = update.message.text

        # پیدا کردن کاربر مقصد
        replied_text = update.message.reply_to_message.text

        for user_id in users:
            if replied_text in replied_text:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=text
                )
                break


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))

app.run_polling()
