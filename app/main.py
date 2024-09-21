
from keyboards import *
from session_db import session_users, session_tasks
from feature import *
from my_token import bot



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

@bot.message_handler(func=lambda message: message.text == "Редактировать сообщение")
def edit_message(message):
    msg = bot.send_message(message.chat.id, 'Введите ID сообщения для редактирования:')
    bot.register_next_step_handler(msg, process_edit_id)

@bot.message_handler(func=lambda message: message.text == "Удалить сообщение")
def delete_message(message):
    user_id = message.chat.id

@bot.message_handler(func=lambda message: message.text == "Показать сообщения")
def show_messages(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_menu_direct())

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




if __name__ == "__main__":
    print('Start App . . .')
    
    bot.polling(none_stop=True)
    print('Stop App . . .')





