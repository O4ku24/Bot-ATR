import telebot
from models import Users

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_name(message):
    msg = bot.send_message(message.chat.id, 'Введи имя:')
    bot.register_next_step_handler(msg)


    



if __name__ == '__main__':
    print('Start Apps . . .')
    bot.infinity_polling()
    print('End Apps . . .')
    

