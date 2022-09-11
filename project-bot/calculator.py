from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def power(a, b):
    return a ** b

def divide(a, b):
    error_message = 'divide by 0'

    if b == 0:
        return error_message
    else:
        return a / b


def operations(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="| + | * | ** | - | / |")


def calculate(operand_a, operand_b, operation):
    result = None
    if operation == '+':
        result = sum(operand_a, operand_b)
    elif operation == '-':
        result = subtract(operand_a, operand_b)
    elif operation == '*':
        result = mul(operand_a, operand_b)
    elif operation == '**':
        result = power(operand_a, operand_b)
    else:
        result = divide(operand_a, operand_b)
    
    return result   

#/calc 15 20 +
def calc(update, context):
    user_input = update.message.text
    user_input = user_input.split()

    arg_1 = user_input[1]
    arg_2 = user_input[2]
    operation = user_input[3]

    result_message = arg_1 + operation + arg_2

    arg_1 = int(arg_1)
    arg_2 = int(arg_2)
    result = calculate(arg_1, arg_2, operation)

    result_message = result_message + ' = ' + str(result)  

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=result_message)

def compare(update, context):
    user_input = update.message.text
    user_input = user_input.split()


    number_1 = int(user_input[1])
    number_2 = int(user_input[2])
    if number_1 > number_2:
        result = 'Перше більше'
    elif number_1 < number_2:
        result = 'Друге більше'
    else:
        result = 'Числа однакові'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=result)



def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This calculator.")


updater = Updater("5623052988:AAG9Zxtek-xPat5LnBjd0zq13Wga_7iYjLo")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", operations))
dispatcher.add_handler(CommandHandler("calc", calc))
dispatcher.add_handler(CommandHandler("compare", compare))

updater.start_polling()
updater.idle()