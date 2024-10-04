
from keyboards import *
from session_db import session
from feature import *
from my_token import bot


#Старт для работы с ботом
@bot.message_handler(commands=['start'])
def start(message):
    session.create_table()
    user_id = message.chat.id
    #входим как разработчик
    if session.get_developer(user_id):
        start_developer(message=message)
        print(f'Enter Developer - {user_id}\n')
    #проверям есть ли пользователь в db как админ
    elif session.get_admin(user_id):
        start_direct(message=message)
        print(f'Enter SuperUser - {user_id}\n')
    #проверяем есть ли пользователь как работник
    elif session.get_user_in_id(user_id):
        start_worker(message=message)
        print(f'Enter User - {user_id}\n')
    #регистрируем user
    else:
        print(f'Enter New User {user_id}\n')
        start_reg_user(message)

# Обработчик полученного контакта
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    get_contact_user(message=message)


    
@bot.message_handler(content_types = 'text')
def enter_commands(message):
    commands ={"Войти как админ":start_direct(message),
               "Войти как":get_worker_list(message),
               "Все задачи":get_tasks_list(message)}
    for answer, value in commands.items():
        print(F'1 - {message.text}')
        if message.text == answer:
            print(F'2 - {answer}')
            bot.send_message(message.chat.id,
                            'hi',
                            reply_markup=value)
        else:
            bot.send_message(message.chat.id,
                            'no')


if __name__ == "__main__":
    print('Start App . . .')
    bot.polling(none_stop=True)
    print('Stop App . . .')

