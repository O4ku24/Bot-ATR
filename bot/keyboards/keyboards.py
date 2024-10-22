from telebot import types
from database.session_db import session



def menu_develeper():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Войти как админ"))
    markup_menu.add(types.KeyboardButton("Войти как"))
    return markup_menu

def main_menu_worker():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Сделать Заявку Для Администратора"))
    markup_menu.add(types.KeyboardButton("Посмотреть Мои Задачи"))
    markup_menu.add(types.KeyboardButton("Изменить Статус Задачи"))
    markup_menu.add(types.KeyboardButton("Изменить Дату Завершения Задачи"))
    markup_menu.add(types.KeyboardButton("Добавить Фото"))
    markup_menu.add(types.KeyboardButton("Деньги"))
    return markup_menu

def main_menu_direct():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Заявки для администратора"))
    markup_menu.add(types.KeyboardButton("Создать задачу для работника"))
    markup_menu.add(types.KeyboardButton("Создать задачу для администратора"))
    markup_menu.add(types.KeyboardButton("Все задачи"))
    return markup_menu

def list_tasks():
    markup_tasks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tasks_id_list = session.get_list_all_tasks()
    for task_id in tasks_id_list:
        markup_tasks.add(types.KeyboardButton((str(task_id)).replace("('",'').replace("',)",'')))
    return markup_tasks

def start_register_user():
    markup_nemu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_nemu.add(types.KeyboardButton("Отправить Свой Контакт", request_contact=True))
    return markup_nemu

def list_worker() -> types.ReplyKeyboardMarkup:
    markup_nemu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    workers_list = session.get_list_all_users()
    for worker in workers_list:
        markup_nemu.add(types.KeyboardButton((str(worker)).replace(',','').replace(')','').replace('(','').replace("'",'')))
    return markup_nemu

def start():
    markup_nemu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_nemu.add(types.KeyboardButton('/Start'))