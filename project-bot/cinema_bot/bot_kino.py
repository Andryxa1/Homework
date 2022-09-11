from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import csv


file_name = 'film.csv'
headers = ['film', 'category', 'age'] 


def create_posters():
    films = [
        ['Матриця', 'бойовик', 16],
        ['Друзі', 'комедія', 12],
        ['Співай', 'мультфільм', 6],
        ['Вічні', 'пригоди', 12]
    ]  

    with open(file_name, 'w', encoding='UTF8', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        writer.writerows(films)



def error_input(update, context):
    message = '''Введеної команди немає: /help - для перегляду доступних команд'''
    update.message.reply_text(message)



def start(update, context):
    if not os.path.exists(file_name):
        create_posters()

    message = '''Вас вітає бот-кіноафіша:
    /help - для перегляду доступних команд'''

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message)



def bot_commands(update, context):   
    message = '''Основні команди [та їх параметри]:
        /posters_list - перегляд фільмів прокв аті
        /posters_add [назва жанр вік] - додати фільм в прокат
        /posters_remove [назва] - зняти фільм з прокату'''

    chat = update.effective_chat
    context.bot.send_message(chat_id = chat.id, text = message) 



def films_list(update, context):
    message = 'Фільми в прокаті:'

    with open(file_name, 'r', encoding='UTF8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            film = "|{:<}|{:<}|{:>}|".format(row['film'], row['category'], row['age'])
            print(film)
            message += "\n" + film


    chat = update.effective_chat
    context.bot.send_message(chat_id = chat.id, text = message) 



def films_add(update, context):
    film_info = update.message.text
    film_info = film_info.split() 


    
    film = dict()
    film['film'] = film_info[1]
    film['category'] = film_info[2]
    film['age'] = film_info[3]

    with open(file_name, 'a', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writerow(film)

    message = '''Фільм додано в прокат. 
    /posters_list - для перегляду списку всіх фільмів'''

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message) 



def films_delete(update, context):
    film_delete = update.message.text
    film_delete = film_delete.split() 
     
    film_name = film_delete[1]
    

    films = []

    with open(file_name, 'r', encoding='UTF8',) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['film'] == film_name:
                continue
            films.append([row['film'], row['category'], row['age']])   

    with open(file_name, 'w', encoding='UTF8', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        writer.writerows(films)        

    message = '''Фільм знято з прокату. 
    /posters_list - для перегляду списку всіх фільмів'''

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message) 


updater = Updater("5502826411:AAECgfxO7huvb8S7mc_Pr3UJMm2s_enVNBo")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", bot_commands))
dispatcher.add_handler(CommandHandler("posters_list", films_list))
dispatcher.add_handler(CommandHandler("posters_add", films_add))
dispatcher.add_handler(CommandHandler("posters_remove", films_delete))
dispatcher.add_handler(MessageHandler(Filters.all, error_input))


updater.start_polling()
updater.idle()