import sqlite3



class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
     

    
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
                       user_id INTEGER PRIMARY KEY,
                       first_name TEXT,
                       last_name TEXT,
                       tg_id INTEGER UNIQUE,
                       post TEXT,
                       phone INTEGER,
                       pin INTEGER
        )
        ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
                       task_id INTEGER,
                       title TEXT,
                       descreption TEXT,
                       status TEXT,
                       start_time  TEXT,
                       end_time TEXT,
                       user_customer_id INTEGER PRIMARY KEY,
                       user_executer_id INTEGER
        )
        ''')
        connect.commit()
        connect.close()

    def connect(self, data: any):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(data)
        connect.commit()
        connect.close()

        





session = Session('database.sqlite3')
session.create_table()
