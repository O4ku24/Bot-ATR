from telebot import types
from session_db import session_users

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
    markup_menu.add(types.KeyboardButton("Войти как работник"))
    return markup_menu

def tasks_menu(tasks_id_list:list[dict[int]:[str]]) -> types.ReplyKeyboardMarkup:
    """ принемает в себя:
        LIST состоящий из 
        DICT в которых 
            ключ это INTEGER  
            значение это STRING """
    markup_tasks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for task_id in tasks_id_list:
        markup_tasks.add(types.KeyboardButton(f'{task_id}'))
    return markup_tasks

def start_register_user():
    markup_nemu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_nemu.add(types.KeyboardButton("Отправить Свой Контакт", request_contact=True))
    return markup_nemu

def list_worker(msg):
    
    markup_nemu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    workers_list = session_users.get_db_list_all_user(msg)
    for worker in workers_list:
        markup_nemu.add(types.KeyboardButton(f'{worker}'))
    return markup_nemu
