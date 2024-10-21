from abc import ABC, abstractmethod
import os
from typing import Any, Dict, List

from app.database.session_db import session

from models_task import ChangeTask, CreateTask
from models_user import ChangeUser, CreateUser

from database.user_db import create_user

class Model(ABC):
    @abstractmethod
    async def all(self) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, data: Any) -> None:
        raise NotImplementedError




class Users(Model):
    def __init__(self, user_id: str,
                 first_name: str,
                 last_name: str,
                 tg_id: int,
                 post: str,
                 phone: int,
                 pin: int):
        self.user_id = user_id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.tg_id = tg_id,
        self.post = post,
        self.phone = phone,
        self.rin = pin
    
    @staticmethod
    def add(user: CreateUser) -> None:
        session.connect(create_user)

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