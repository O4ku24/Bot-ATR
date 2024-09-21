import telebot
from keyboards import *
from session_db import session_users, session_tasks
from dotenv import load_dotenv
import time
from feature import *

""" load_dotenv()
TOKEN = os.getenv('TOKEN') """

bot = telebot.TeleBot('6105146346:AAFcm1CVVly8GllMD_KXDBw0iF20x6RiW8g')



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if session_users.get_db_user(user_id):
        start_direct(message)
    else:
        start_worker(message)


@bot.message_handler(func=lambda message: message.text == "Посмотреть Мои Задачи")
def tasks_menu_worker(message):
    db_tasks_list = session_tasks.get_db_tasks_list(user_id=message.chat.id)
    tasks_list = []
    if db_tasks_list:
        for msg in db_tasks_list:
            tasks_list.append(1)   
    else:
        bot.send_message(message.chat.id, 'У вас нет сохранённых сообщений.')
    tasks_menu(tasks_list)


def process_save(message):
    user_text = message.text
    user_id = message.from_user.id

    
    session_tasks.create_db_task(user_text, 'err', 'err', f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}', '21.10.2024', user_id)

    bot.send_message(message.chat.id, 'Ваша задача сохранена!')
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())


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

"""     # Редактирование записи в базе данных
    cursor.execute('UPDATE messages SET message = ? WHERE id = ? AND user_id = ?', (new_message, entry_id, user_id))
    if cursor.rowcount > 0:
        conn.commit()
        bot.send_message(message.chat.id, 'Информация успешно отредактирована!')
    else:
        bot.send_message(message.chat.id, 'Запись с таким ID не найдена.')
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())


@bot.message_handler(func=lambda message: message.text == "Удалить сообщение")
def delete_message(message):
    user_id = message.chat.id
    cursor.execute('SELECT id, message FROM messages WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    tasks_list = []
    if messages:
        for msg in messages:
            tasks_list.append({msg[0]:msg[1]})   
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

    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())


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
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())
#reply_markup=get_contact_keyboard() """


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





