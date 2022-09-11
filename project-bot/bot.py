# pip install python-telegram-bot

# https://core.telegram.org/bots/api

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-–-Your-first-Bot

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Types-of-Handlers

# https://docs.python-telegram-bot.org/en/v13.13/telegram.bot.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.updater.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.dispatcher.html

# https://docs.python-telegram-bot.org/en/v13.13/telegram.update.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.callbackcontext.html


# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.messagehandler.html
# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import logging
updater = Updater(token='5712335023:AAFRHis6MhiUeiKk4YowGPQ-EgxMeUbvPjg', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()
updater.idle()