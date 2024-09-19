import sqlite3
import time


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
        print('tyt')
        cursor = connect.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                       name TEXT,
                       user_id  INTEGER PRIMARY KEY,
                       post TEXT,
                       phone INTEGER UNIQUE,
                       password TEXT
        )
        ''')
        cursor.execute('INSERT INTO Users (name, user_id, post, phone, password) VALUES (?,?,?,?,?)', 
                       (user_name, user_id, post, number_phone, password))
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


session = Session('bot.db')


""" session.create_db_user(user_name='admin',
                            user_id=549725325,
                            post='admin',
                            number_phone='+79233302882',
                            password='6552')

session.create_db_task(title='Написать бота',
                            descreption='С кнопками и все самым лучшим',
                            status='В процессе',
                            start_time=f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}',
                            end_time='1.10.2024',
                            user_id=549725325)   """                        



