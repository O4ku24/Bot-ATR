
from pydantic import BaseModel

class Task(BaseModel):
    task_id: int
    title: str
    decreption: str
    status: str
    start_time: str
    end_time: str
    user_customer_id: int
    user_executor_id: int

class CreateTask(BaseModel):
    task_id: int    
    title: str
    decreption: str
    status: str
    start_time: str
    end_time: str
    user_customer_id: int
    user_executor_id: int

class ChangeTask(BaseModel):
    task_id: int 
    decreption: str  
    status: str
    end_time: str
    user_executor_id: int


