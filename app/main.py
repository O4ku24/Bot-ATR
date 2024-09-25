
from keyboards import *
from session_db import session_users
from feature import *
from my_token import bot

#Старт для работы с ботом
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    #входим как разработчик
    if session_users.get_db_developer(user_id):
        start_developer(message=message)
        print(f'Enter Developer - {user_id}')
    #проверям есть ли пользователь в db как админ
    elif session_users.get_db_admin(user_id):
        start_direct(message=message)
        print(f'Enter SuperUser - {user_id}')
    #проверяем есть ли пользователь как работник
    elif session_users.get_db_user_in_id(user_id):
        start_worker(message=message)
        print(f'Enter User - {user_id}')
    #регистрируем user
    else:
        print(f'Enter New User {user_id}')
        start_reg_user(message)

# Обработчик полученного контакта
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    get_contact_user(message=message)

    
@bot.message_handler(content_types = 'text')
def enter_dev_commands(msg):
    if msg.text == "Войти как админ":
        start_direct(msg)

    elif msg.text == "Войти как":
        list_worker(msg)

    

if __name__ == "__main__":
    print('Start App . . .')
    
    bot.polling(none_stop=True)
    print('Stop App . . .')





