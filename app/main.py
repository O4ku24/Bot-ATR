import telebot
from telebot import types
from session_db import session
from dotenv import load_dotenv
import os
from session_db import session
import sqlite3

""" load_dotenv()
TOKEN = os.getenv('TOKEN') """

bot = telebot.TeleBot('6105146346:AAFcm1CVVly8GllMD_KXDBw0iF20x6RiW8g')


    
# Создание или подключение к базе данных SQLite
conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT
)
''')
conn.commit()


# Функция для отображения клавиатуры с кнопками
def main_menu():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Сохранить сообщение"))
    markup_menu.add(types.KeyboardButton("Редактировать сообщение"))
    markup_menu.add(types.KeyboardButton("Удалить сообщение"))
    markup_menu.add(types.KeyboardButton("Показать сообщения"))
    markup_menu.add(types.KeyboardButton(''))
    return markup_menu

def tasks_menu(tasks_id_list:list[dict[int]:[str]]):
    markup_tasks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for task_id in tasks_id_list:
        markup_tasks.add(types.KeyboardButton(f'{task_id}'))
        print(task_id)
    return markup_tasks


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Здравствуйте! Используйте кнопки для взаимодействия с ботом.',
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: message.text == "Сохранить сообщение")
def save_message(message):
    msg = bot.send_message(message.chat.id, 'Введите сообщение для сохранения:')
    bot.register_next_step_handler(msg, process_save)


def process_save(message):
    user_text = message.text
    user_id = message.from_user.id

    # Сохранение информации в базе данных
    cursor.execute('INSERT INTO messages (user_id, message) VALUES (?, ?)', (user_id, user_text))
    conn.commit()

    bot.send_message(message.chat.id, 'Ваша информация сохранена!')
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Редактировать сообщение")
def edit_message(message):
    msg = bot.send_message(message.chat.id, 'Введите ID сообщения для редактирования:')
    bot.register_next_step_handler(msg, process_edit_id)


def process_edit_id(message):
    entry_id = message.text
    msg = bot.send_message(message.chat.id, 'Введите новое сообщение:')
    bot.register_next_step_handler(msg, process_edit_message, entry_id)


def process_edit_message(message, entry_id):
    new_message = message.text
    user_id = message.from_user.id

    # Редактирование записи в базе данных
    cursor.execute('UPDATE messages SET message = ? WHERE id = ? AND user_id = ?', (new_message, entry_id, user_id))
    if cursor.rowcount > 0:
        conn.commit()
        bot.send_message(message.chat.id, 'Информация успешно отредактирована!')
    else:
        bot.send_message(message.chat.id, 'Запись с таким ID не найдена.')
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Удалить сообщение")
def delete_message(message):
    user_id = message.chat.id
    cursor.execute('SELECT id, message FROM messages WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    tasks_list = []
    if messages:
        for msg in messages:
            tasks_list.append({msg[0]:msg[1]})
        print(tasks_list)    
    else:
        bot.send_message(user_id, 'У вас нет сохранённых сообщений.')
    msg = bot.send_message(message.chat.id, 'Выберете ID сообщения для удаления:', reply_markup=tasks_menu(tasks_id_list=tasks_list))
    bot.register_next_step_handler(msg, process_delete)


def process_delete(message):
    entry_id = message.text[0]
    user_id = message.from_user.id

    # Удаление записи из базы данных
    cursor.execute('DELETE FROM messages WHERE id = ? AND user_id = ?', (entry_id, user_id))
    if cursor.rowcount > 0:
        conn.commit()
        bot.send_message(message.chat.id, 'Информация успешно удалена!')
    else:
        bot.send_message(message.chat.id, 'Запись с таким ID не найдена.')

    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Показать сообщения")
def show_messages(message):
    user_id = message.from_user.id
    cursor.execute('SELECT id, message FROM messages WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    if messages:
        msg_text = 'Ваши сообщения:\n'
        for msg in messages:
            msg_text += f'ID: {msg[0]}, Сообщение: {msg[1]}\n'
    else:
        msg_text = 'У вас нет сохранённых сообщений.'

    bot.send_message(message.chat.id, msg_text)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu())
#reply_markup=get_contact_keyboard()


""" def get_contact_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button = types.KeyboardButton("Поделиться контактной информацией", request_contact=True)
    keyboard.add(button)
    return keyboard


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    contact = message.contact
    bot.reply_to(message, f"Спасибо! Вот твой контакт:\n"
                          f"Имя: {contact.first_name} {contact.last_name}\n"
                          f"Номер телефона: {contact.phone_number}\n"
                          f"ID: {message.chat.id}")
    print(f"Имя: {contact.first_name} {contact.last_name}\n"
          f"Номер телефона: {contact.phone_number}\n"
          f"ID: {message.chat.id}")
 """



if __name__ == "__main__":
    print('Start App . . .')
    bot.polling(none_stop=True)
    print('Stop App . . .')

def close_connection():
    conn.close()

import atexit
atexit.register(close_connection)



