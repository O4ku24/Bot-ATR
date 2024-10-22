from dotenv import load_dotenv
import os
import telebot

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

