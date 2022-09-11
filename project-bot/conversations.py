
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    CallbackContext, 
    MessageHandler, 
    Filters
)

user_data = dict()

STEP_ONE, STEP_TWO, STEP_THREE, STEP_FOUR = range(4)


def start(update: Update, context: CallbackContext) -> None:
    




    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Введіть необхідну інформацію", reply_markup=reply_markup)


    

def user_name(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="enter your name ")
    return STEP_TWO


def user_email(update, context):
    chat = update.effective_chat
    user_data['name'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your email ")
    return STEP_THREE    


def user_phone(update, context):
    chat = update.effective_chat
    user_data['mail'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your phone ")
    return STEP_FOUR    


def user_finish(update, context):
    chat = update.effective_chat
    user_data['phone'] = update.message.text

    user_text = "Thanks " + user_data.get('name') + " 😉"

    context.bot.send_message(chat_id=chat.id, text=user_text)
    return ConversationHandler.END  


def cancel(update, context):
    update.message.reply_text('Cancelled by user. Send /menu to start again')
    return ConversationHandler.END


def main() -> None:
    updater = Updater(token='5711149967:AAHBEF40oUM6JNLsMudUmxrSJzZNPMSgX0s')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    branch_user_handler = ConversationHandler(
        entry_points = [CallbackQueryHandler(user_name, 'user_info')], 
        states={

            STEP_TWO:   [MessageHandler(Filters.text & (~ Filters.command), user_email)],
            STEP_THREE: [MessageHandler(Filters.text & (~ Filters.command), user_phone)],
            STEP_FOUR:  [MessageHandler(Filters.text & (~ Filters.command), user_finish)]
        }, 
        fallbacks=[CommandHandler("stop", cancel)]
    )

    dispatcher.add_handler(branch_user_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()