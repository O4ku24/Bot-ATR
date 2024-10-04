import sqlite3


class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
     
#Create User
    def create_user(self,
                    user_name:str, 
                    user_id:int, 
                    post:str, 
                    number_phone:str, 
                    password:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                       name TEXT,
                       user_id  INTEGER PRIMARY KEY,
                       post TEXT,
                       phone INTEGER UNIQUE,
                       password TEXT
        )
        ''')
        cursor.execute('INSERT INTO Users (name,    user_id,   post,   phone,          password) VALUES (?,?,?,?,?)', 
                                        (user_name, user_id,   post,   number_phone,   password))
        connect.commit()
        
        connect.close()
    
#Create Task
    def create_task(self, 
                       title:str,
                       descreption:str,
                       status:str,
                       start_time:str,
                       end_time:str,
                       user_id:int):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
                       title TEXT,
                       descreption TEXT,
                       status TEXT,
                       start_time  TEXT,
                       end_time TEXT,
                       user_id INTEGER PRIMARY KEY
        )
        ''')
        cursor.execute('INSERT INTO Tasks (title, descreption, status, start_time, end_time, user_id) VALUES (?,?,?,?,?,?)', 
                       (title, 
                        descreption, 
                        status, 
                        start_time, 
                        end_time, 
                        user_id))
        connect.commit()
        connect.close()

#Get Admin
    def get_admin(self, user_id):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Users WHERE user_id = {user_id} AND post = "admin"')
        if cursor.fetchall():   
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

#Get List All Tasks
    def get_list_all_tasks(self):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM Tasks ')
        list_all_tasks = cursor.fetchall()
        return list_all_tasks

#Create Table
    def create_table(self):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                       name TEXT,
                       user_id  INTEGER PRIMARY KEY,
                       post TEXT,
                       phone INTEGER UNIQUE,
                       password TEXT
        )
        ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
                       title TEXT,
                       descreption TEXT,
                       status TEXT,
                       start_time  TEXT,
                       end_time TEXT,
                       user_id INTEGER PRIMARY KEY
        )
        ''')
        connect.commit()
        connect.close()




session = Session('database.sqlite3')
