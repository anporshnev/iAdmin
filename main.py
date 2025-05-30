import uvicorn
from fastapi import FastAPI

from app.api.endpoints.room import room_router
from app.config import settings

app = FastAPI()
app.include_router(room_router)

if __name__ == '__main__':
    uvicorn.run(app='main:app')