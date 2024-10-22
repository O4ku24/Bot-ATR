import sqlite3



class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
     

    


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
