from my_token import bot
from keyboards import *
import time
from session_db import session_users
import random

time_now = f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}'

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

def get_worker_list(msg):
    worker_list = list_worker(msg)
    return bot.send_message(msg.chat.id, 'Enter User: ', reply_markup=worker_list)

def get_contact_user(message):
    contact = message.contact
    user_id = message.chat.id
    print(user_id)
    post = 'dev'#сюда надо добавить функцию по поиску должности по номеру телефона который будет выдавать админ
    password = random.randint(1000, 9999)
    session_users.create_db_user(contact.first_name, message.chat.id, post, contact.phone_number, password)
    print(f'New User Create:\nname: {contact.first_name}\nNumber: {contact.phone_number}')
    return bot.reply_to(user_id, f"Спасибо! Вот твой контакт:\n"
                          f"Имя: {contact.first_name} {contact.last_name}\n"
                          f"Номер телефона: {contact.phone_number}\n"
                          f"Твой пароль для WEB-версии: {password}")

