import sqlite3


class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
     
  
    def create_db_user(self,
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
    
    def create_db_task(self, 
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

    def get_db_admin(self, user_id):
        conn = sqlite3.connect('bot.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Users WHERE user_id = {user_id} AND post = "admin"')
        if cursor.fetchall():   
            return True
        else:
            return False
    
    def get_db_developer(self, user_id):
        conn = sqlite3.connect('bot.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Users WHERE user_id = {user_id} AND post = "dev"')
        if cursor.fetchall():   
            return True
        else:
            return False
        
    def get_db_user_in_id(self, user_id):
        conn = sqlite3.connect('bot.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM Users WHERE user_id = ? AND post = "work"', (user_id,))
        if cursor.fetchall():
            return True
        else:
            return False
    
    def get_db_list_all_user(self):
        conn = sqlite3.connect('bot.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users')
        list_all_users = cursor.fetchall()
        return list_all_users

    def get_db_list_all_tasks(self):
        conn = sqlite3.connect('bot.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Tasks ')
        list_all_tasks = cursor.fetchall()
        return list_all_tasks
    
    def create_table_db_users(self):
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
        connect.commit()
        connect.close()

    def creare_table_db_tasks(self):
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
        connect.commit()
        connect.close()


session_users = Session('bot.db')
session_tasks = Session('bot.db')




