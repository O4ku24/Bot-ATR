import telebot
import json
from telebot import types



bot = telebot.TeleBot('token')

""" 
@bot.message_handler(func=lambda m: True)
def get_text_messege(message):
    text:str = message.text
    print(text)
    with open ('db.json', 'w', encoding='utf-8') as session:
        json.dump(text, session) """

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    bt_1 = types.KeyboardButton("Шалыгин", request_contact=True)
    bt_2 = types.KeyboardButton("Толстый",request_contact=True)
    markup.add(bt_1)
    markup.add(bt_2)
    bot.send_message(message.chat.id, 'привет', format(message.from_user), reply_markup=markup)
    
    print(message.text)
    if message.text == '/start':
        print('tyt')
        with open('db.json', 'r', encoding='utf-8') as session:
            data = json.load(session)
            task = (data["users"]["1"]["tasks"]["1"]["task"])
            descreption = (data["users"]["1"]["tasks"]["1"]["descreption"])

            bot.reply_to(message= message, text=task)
""" 
@bot.get_my_commands(scope=None)
def get_my_commands():
    pass """
#get_task_user_id(message='/tasks')



"""     if message.text == 'text':
        print('tyt2')
        bot.send_message(message.from_user.id, "напиши команду 1")
        input_1:str = message.text
        print(bot.send_message(message.from_user.id))
        print(input_1)
    elif message.text == "/help":
        print('tyt3')
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        print('tyt4')
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.") """
	
""" @bot.message_handler(json)
def echo_all(message):
    bot.reply_to(message, message.text)
    print('tyt2') """



bot.polling(non_stop=True)



