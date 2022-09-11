
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3"),
        InlineKeyboardButton("Option 4", callback_data="4"),],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Зробіть ваш вибір:", reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""

    updater = Updater(token='5772408653:AAEqDN4-Uayp9xhHvqHE1Xv469xxXGkDOHs')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()