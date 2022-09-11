import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    CallbackContext
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Callback data
ONE, TWO, THREE, FOUR = range(4)


def start(update: Update, context: CallbackContext) -> None:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("пункт 1", callback_data=str(ONE)),
            InlineKeyboardButton("пункт 2", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Головне меню", reply_markup=reply_markup)


def one(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("варіант 3", callback_data=str(THREE)),
            InlineKeyboardButton("варіант 4", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Виберіть, що вас цікавить", reply_markup=reply_markup
    )


def two(update: Update, context: CallbackContext) -> int:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="ви вибрали варіант 2")


def three(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="ви вибрали варіант 3")


def four(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="ви вибрали варіант 4")



def main() -> None:
    """Run the bot."""
    updater = Updater(token='5772408653:AAEqDN4-Uayp9xhHvqHE1Xv469xxXGkDOHs')
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"))
    dispatcher.add_handler(CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"))
    dispatcher.add_handler(CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"))
    dispatcher.add_handler(CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"))


    # Run the bot until the user presses Ctrl-C
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()