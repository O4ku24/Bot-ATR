from session_db import session_users, session_tasks

list_task = session_tasks.get_db_list_all_tasks()
for i in list_task:
    print(i)
