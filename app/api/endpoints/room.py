from fastapi import APIRouter


room_router = APIRouter(
    prefix='/room',
    tags=['Room']
)

@room_router.get('/')
async def get_rooms():
    pass

@room_router.post('/')
async def create_room():
    pass