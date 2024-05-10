from telegram.ext import CommandHandler, CallbackContext, ContextTypes, Application, MessageHandler, filters
from telegram import Update
from token_1 import test_token
from models import Users
from Connect import session_user, session_task


async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    task = update.message.text
    user_name = update.message.chat.first_name
    await update.message.reply_text(f'Привет! {user_name}')
    print(f'Вошел {user_id}, {user_name}')
    session_user.add_new_user(user_id, user_name)
    ver_user = session_user.get_user(user_id)
    if ver_user == False:
        session_user.add_new_user(user_id, user_name)
        session_task.add_new_task(user_id, task)
    else:
        session_task.add_new_task(user_id, task)

async def add_task(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(user_id = update.message.chat.id, task = update.message.text)
    print(f'1{task, user_id}')
    task:str = update.message.text
    user_id:int = update.message.chat.id
    print(f'{task, user_id}')
    print(f'запись {user_id, task}')
    session_task.add_new_task(user_id, task)



  
            
def main():
    app = Application.builder().token(test_token.get_token()).build()
    app.add_handler(CommandHandler('Start', start))
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), add_task)
    #app.add_handler(CommandHandler('Task', add_task))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    print('Strt Bot...')
    main()
    print('Stopet Bot...')





    

    
        
        






