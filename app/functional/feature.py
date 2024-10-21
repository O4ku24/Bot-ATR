from my_token import bot
from app.keyboards.keyboards import *
from app.database.session_db import session
import random

#time_now = f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}'

def start_developer(message):
    bot.send_message(
        message.chat.id,
        'Hi Developer!',
        reply_markup=menu_develeper()
    )

def start_worker(message):
    bot.send_message(
        message.chat.id,
        'Здравствуйте! Используйте кнопки для взаимодействия с ботом.',
        reply_markup=main_menu_worker()
    )

def start_direct(message):
    bot.send_message(
        message.chat.id,
        'Здравствуй БОСС!!! С чего начнем кошмарить собак?',
        reply_markup=main_menu_direct()
    )

def start_reg_user(message):
    bot.send_message(
        message.chat.id, 'Отправь Свой Контакт',
        reply_markup=start_register_user()
    )

def get_worker_list(message):
    bot.send_message(
        message.chat.id, 
        'Команда принята!', 
        reply_markup=list_worker())
    
def get_tasks_list(message):
    bot.send_message(
        message.chat.id,
        'Команда принята!',
        reply_markup=list_tasks()
    )

def get_contact_user(message):
    contact = message.contact
    user_id = message.chat.id
    post = 'dev'#сюда надо добавить функцию по поиску должности по номеру телефона который будет выдавать админ
    password = random.randint(1000, 9999)
    session.create_user(contact.first_name, message.chat.id, post, contact.phone_number, password)
    
    print(f'New User Create:\nname: {contact.first_name}\nNumber: {contact.phone_number}')
    return bot.send_message(user_id, f"Отлично! \nТвой логин: {contact.phone_number} \nТвой пароль для WEB-версии: {password}", reply_markup=start())

def add_task(msg):
    contact = msg.contact
    user_id = msg.chat.id
