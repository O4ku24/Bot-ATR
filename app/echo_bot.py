
import sqlite3
from Connect import session_user, session_task

def get_user(self, id) -> str:
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        author_ids = [x[0] for x in cursor.execute("select telegram_id from Users").fetchall()]
        print(author_ids)
        if id in author_ids:
            return True
        else:
            return False

ver_user = session_user.get_user(1231627112)
print(ver_user)
