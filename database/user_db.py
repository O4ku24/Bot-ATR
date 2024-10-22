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

#Get Admin
def get_admin(user: CreateUser):
    user_admin = session.connect(f'SELECT * FROM Users WHERE tg_id = {user.tg_id} AND post = "admin"')
    if user_admin:   
        return True
    else:
        return False

#Get Developer
def get_developer(self, user_id):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Users WHERE user_id = {user_id} AND post = "dev"')
        if cursor.fetchall():   
            return True
        else:
            return False

#Get User In ID
def get_user_in_id(self, user_id):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM Users WHERE user_id = ? AND post = "work"', (user_id,))
        if cursor.fetchall():
            return True
        else:
            return False

#Get List All Users
def get_list_all_users(self):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM Users')
        list_all_users = cursor.fetchall()
        return list_all_users

        