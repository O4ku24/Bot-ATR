from main import bot
from keyboards import *

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

