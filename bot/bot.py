import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Get the Telegram bot token from the environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Telegram bot token not found in the .env file.")

# Create the bot using the token from the environment variable
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Create the updater using the token from the environment variable
updater = Updater(bot.token, use_context=True)

ROOM_NUMBER, PHONE_NUMBER, RESERVING = range(3)
user_data = {}


def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id

    if chat_id not in user_data:
        user_data[chat_id] = {}
        update.message.reply_text(
            f"Hello {user.first_name}! Please enter your room number:")
        return ROOM_NUMBER
    else:
        update.message.reply_text("You are already registered!")


def room_number(update, context):
    chat_id = update.message.chat_id
    room_number = update.message.text
    user_data[chat_id]['room_number'] = room_number
    update.message.reply_text("Great! Now, please enter your phone number:")
    return PHONE_NUMBER


def phone_number(update, context):
    chat_id = update.message.chat_id
    phone_number = update.message.text
    user_data[chat_id]['phone_number'] = phone_number

    keyboard = [[InlineKeyboardButton("15 minutes before ⏰", callback_data='15'),
                 InlineKeyboardButton("On time ⏰", callback_data='0')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Please choose your notification preference:",
        reply_markup=reply_markup
    )
    return RESERVING


def reservation(update, context):
    query = update.callback_query
    context.user_data['notification_preference'] = int(query.data)
    query.edit_message_text(text="You selected: {}".format(query.data))
    return RESERVING


def cancel(update, context):
    update.message.reply_text("Reservation canceled.")
    context.user_data.clear()


def main():
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ROOM_NUMBER: [MessageHandler(filters.text & ~filters.command, room_number)],
            PHONE_NUMBER: [MessageHandler(filters.text & ~filters.command, phone_number)],
            RESERVING: [CallbackQueryHandler(reservation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    return updater


if __name__ == "__main__":
    # Start the Telegram bot
    updater.start_polling()
    updater.idle()
