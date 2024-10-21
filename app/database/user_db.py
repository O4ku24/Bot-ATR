from session_db import session
from models.models import ChangeUser, CreateUser


#Create User
def create_user(user: CreateUser):
    session.connect('INSERT INTO Users (user_id, first_name, last_name, tg_id, post, phone, pin) VALUES (?,?,?,?,?)', 
                        (user.user_id, 
                         user.first_name,
                         user.last_name,
                         user.tg_id,
                         user.post,
                         user.phone,
                         user.pin))
    
def change_user(user: ChangeUser):
    session.connect
        