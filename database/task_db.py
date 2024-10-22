from database.session_db import session
from models.models import ChangeTask, CreateTask


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


#Get List All Tasks
    def get_list_all_tasks(self):
        conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM Tasks ')
        list_all_tasks = cursor.fetchall()
        return list_all_tasks