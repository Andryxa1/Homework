# https://pypi.org/project/wikipedia/
# https://pypi.org/project/beautifulsoup4/
# https://pypi.org/project/requests/

import requests
import wikipedia
from bs4 import BeautifulSoup

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, ConversationHandler, MessageHandler, Filters  


wikipedia.set_lang('uk')
print("start wikibot")


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    chat = update.effective_chat

    buttons = [[
            KeyboardButton("/article"),
            KeyboardButton("/random"),
    ]]

    context.bot.send_message(chat_id=chat.id, text="Доброго дня! Що ви хочете зробити:", reply_markup=ReplyKeyboardMarkup(buttons))


def cancel(update):
    """cancels the command if something went wrong"""

    update.message.reply_text(
        'Cancelled by user. Send /make_a_note to start again')
    return ConversationHandler.END


def user_article_title(update: Update, context: CallbackContext) -> int:
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Введіть тему")
    return 2


def user_article_result(update: Update, context: CallbackContext) -> int:
    try:
        word = update.message.text
        print(word)
        search_on_wikipedia = wikipedia.summary(word)

        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text=search_on_wikipedia)
    except Exception:
        context.bot.send_message(chat_id=chat.id, text="Телеграм бот не може знайти статтю")



def random_article(update: Update, context: CallbackContext):
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    url = "https://en.wikipedia.org/wiki/%s" % title
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=url)



article_handler = ConversationHandler(
    entry_points=[CommandHandler('article', user_article_title)],
    states={
        2: [MessageHandler(Filters.text & (~ Filters.command), user_article_result)]
    },
    fallbacks=[CommandHandler('cancel', start)]
)

def main() -> None:
    updater = Updater(token='5635826394:AAHx2eZLVBQjbS53cZ2o1yqqxqTER9-wXGM')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("random", random_article))

    dispatcher.add_handler(article_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()