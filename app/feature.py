from main import bot
from keyboards import *
from session_db import session_tasks, session_users
import time

time_now = f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}'


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

def process_save(message):
    user_text = message.text
    user_id = message.from_user.id
    session_tasks.create_db_task(user_text, 'err', 'err', time_now , '21.12.2024', user_id)
    bot.send_message(message.chat.id, 'Ваша задача сохранена!')
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())

def process_edit_id(message):
    entry_id = message.text
    msg = bot.send_message(message.chat.id, 'Введите новое сообщение:')
    bot.register_next_step_handler(msg, process_edit_message, entry_id)

def process_edit_message(message, entry_id):
    new_message = message.text
    user_id = message.from_user.id

def get_contact_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button = types.KeyboardButton("Поделиться контактной информацией", request_contact=True)
    keyboard.add(button)
    return keyboard

def process_delete(message):
    entry_id = message.text[0]
    user_id = message.from_user.id

