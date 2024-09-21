from telebot import types

def main_menu_worker():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Сделать Заявку На Матерьялы"))
    markup_menu.add(types.KeyboardButton("Посмотреть Мои Задачи"))
    markup_menu.add(types.KeyboardButton("Изменить Статус Задачи"))
    markup_menu.add(types.KeyboardButton("Изменить Дату Завершения Задачи"))
    markup_menu.add(types.KeyboardButton("Добавить Фото"))
    markup_menu.add(types.KeyboardButton("Деньги"))
    return markup_menu

def main_menu_direct():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Кто чем занят"))
    markup_menu.add(types.KeyboardButton("Кому хуев вставить"))
    markup_menu.add(types.KeyboardButton("Статусы Заданий"))
    return markup_menu

def tasks_menu(tasks_id_list:list[dict[int]:[str]]):
    markup_tasks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for task_id in tasks_id_list:
        markup_tasks.add(types.KeyboardButton(f'{task_id}'))
        print(task_id)
    return markup_tasks
