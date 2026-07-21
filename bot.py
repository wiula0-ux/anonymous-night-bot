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

    async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    users[update.message.message_id] = user.id

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"پیام جدید:\n\n{update.message.text}"
    )

    await update.message.reply_text(
        "𝐘𝐨𝐮𝐫 𝐰𝐨𝐫𝐝𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐜𝐚𝐫𝐫𝐢𝐞𝐝 𝐢𝐧 𝐬𝐢𝐥𝐞𝐧𝐜𝐞."
    )
    
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))

app.run_polling()
