from fastapi import APIRouter
from .models import Users
from src.server.users.resolvers import get_user, add_user, update_user, delete_user

router = APIRouter()

@router.get('/')
def get_users():
    return get_user()

@router.post('/')
def add_user(new_user: Users):
    return add_user(new_user)

@router.put('/{user_id}')
def update_user(user_id: int, new_user: Users):
    return update_user(user_id, new_user)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return delete_user(user_id)