
from session_db import session


class Users():
    def __init__(self, 
                 user_name:str, 
                 user_id:str, 
                 post:str, 
                 number_phone:str, 
                 password:str
                 ) -> None:
        self.name = user_name
        self._user_id = user_id
        self.post = post
        self._phone = number_phone
        self._password = password
    
    def __repr__(self) -> str:
        return f'{self}'
    
    def create_user(self):
        session.create_db_user(user_name=self.name,
                               user_id=self._user_id,
                               post=self.post,
                               number_phone=self._phone,
                               password=self._password)
        print(f'Create User {self.name}')
        

    def get_user():
        pass

    def edit_user():
        pass

    def del_user():
        pass




class Tasks():
    def __init__(self, 
                 title:str, 
                 descreption:str, 
                 status:str, 
                 start_time:int, 
                 end_time:int, 
                 user_id:str, 
                 ) -> None:
        self.title = title
        self.descreption = descreption
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.worker = user_id

    def get_task():
        pass

    def create_task():
        pass

    def edit_task():
        pass

    def del_task():
        pass