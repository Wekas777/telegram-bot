import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8495594255:AAENMWNgyRNHUN5sLSIg3rR0dPgJtb_jqNs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("👑 Моё лс", url="tg://user?id=7993659848"),
            InlineKeyboardButton("💬 Задать вопрос", callback_data="ask_question")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message_text = (
        "👋 ВАСАП МАБОЙ, ниже кнопка для перехода ко мне в лс\n\n"
        "💼 *Инструкция как перейти ко мне в лс, для особо тупых:*\n"
        "1. Нажмите кнопку 'Моё лс' для перехода в диалог\n"
        "2. ПОНЯЛ МЕНЯ?\n\n"
        "📞 Я всегда готов помочь тебе! (на самом деле нет)"
    )
    
    await update.message.reply_text(message_text, reply_markup=reply_markup, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "ask_question":
        keyboard = [[InlineKeyboardButton("Моё лс", url="https://t.me/wekas_hlorka")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text="📝 Нажмите кнопку ниже, чтобы написать мне (wekas) 👇",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

def main() -> None:
    # Создаем Application без JobQueue
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()