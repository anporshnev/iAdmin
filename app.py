from fastapi import FastAPI

from app.config import settings

app = FastAPI()

@app.get('/')
def index():

    return {'message': settings.db_settings.db_url}