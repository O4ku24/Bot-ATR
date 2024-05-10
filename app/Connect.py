import sqlite3

class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
    
        
    def add_new_user(self, id:int, user_name:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                       id  INTEGER PRIMARY KEY,
                       telegram_id INTEGER UNIQUE,
                       user_name TEXT
        )
        ''')
        cursor.execute('INSERT INTO Users (telegram_id, user_name) VALUES (?,?)', (id, user_name))
        connect.commit()
        
        connect.close()
    
    def add_new_task(self, id:int, task:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
                       id  INTEGER PRIMARY KEY,
                       telegram_id INTEGER UNIQUE,
                       task TEXT
                       
        )
        ''')
        cursor.execute('INSERT INTO Tasks (telegram_id, task) VALUES (?,?)', (id, task))
        connect.commit()
        connect.close()

    def get_user(self, id) -> str:
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        author_ids = [x[0] for x in cursor.execute("select telegram_id from Users").fetchall()]
        if id in author_ids:
            return True
        else:
            return False


    def get_task(self, id):
        pass
        

session_user = Session('Users.db')
session_task = Session('Tasks.db')

#print(session_user.get_user(549725325))