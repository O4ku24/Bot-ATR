import uvicorn
from fastapi import FastAPI

from app.routers.router import router
from app.urls.urls import url

from bot.bot import bot


app = FastAPI(title='IT-Room',
              version='0.0.1')

app.include_router(router)
app.include_router(url)






if __name__ == '__main__':
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')