import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# التوكن - سوف نضيفه لاحقاً
BOT_TOKEN = os.getenv('8530212894:AAE7n_nv_qz7b2CaMOaHS4m5RkLbfvNDA2w')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("💰 الإيداع", callback_data="deposit")],
        [InlineKeyboardButton("📈 الأرباح", callback_data="profits")],
        [InlineKeyboardButton("💳 السحب", callback_data="withdraw")],
        [InlineKeyboardButton("💼 الرصيد", callback_data="balance")]
    ]
    
    await update.message.reply_text(
        f"🎯 أهلاً بك {user.first_name}!\n\n"
        "هذا بوت استثماري تجريبي\n"
        "اختر من الخيارات:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "deposit":
        await query.edit_message_text("💰 قسم الإيداع قيد التطوير")
    elif query.data == "profits":
        await query.edit_message_text("📈 قسم الأرباح قيد التطوير")
    elif query.data == "withdraw":
        await query.edit_message_text("💳 قسم السحب قيد التطوير")
    elif query.data == "balance":
        await query.edit_message_text("💼 قسم الرصيد قيد التطوير")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    
    print("🤖 البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()
