
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    first_name: str 
    last_name: str
    tg_id: int
    post: str
    phone: int
    pin: int

class CreateUser(BaseModel):
    user_id: int
    first_name: str 
    last_name: str
    tg_id: int
    post: str
    phone: int
    pin: int


class ChangeUser(BaseModel):
    user_id: int
    post: str
    phone: str
    pin: int