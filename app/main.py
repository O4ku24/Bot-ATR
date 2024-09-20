import telebot
from telebot import types
from dotenv import load_dotenv
import os
from session_db import session

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет!")
    

#reply_markup=get_contact_keyboard()


def get_contact_keyboard():
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




if __name__ == "__main__":
    print('Start App . . .')
    bot.polling(none_stop=True)
    print('Stop App . . .')



