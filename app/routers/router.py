
from fastapi import APIRouter, Request
from database.session_db import session

router = APIRouter(prefix='/api')



@router.get('/user/')
def get_list_task(request:Request):
    
    return 'user'
