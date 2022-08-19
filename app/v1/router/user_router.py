from fastapi import APIRouter, Depends, status, Body, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_204_NO_CONTENT
from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.service import auth_service
from app.v1.model.user_model import User
from app.v1.schema.toke_schema import Token
from app.v1.utils.db import Session
from typing import List

session = Session()
user_route = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)

login_route = APIRouter (
    prefix="/api",
    tags=["login"]
)

@user_route.get('/user/', response_model=List[user_schema.User])
def get_users():
    return session.query(User.id,
                        User.username,
                        User.email).all()

@user_route.get('/user/{id}/', response_model=user_schema.User)
def get_user(id: int):
    return session.query(User.id,
                        User.username,
                        User.email).filter(User.id == id).first()

@user_route.post(
    '/user',
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    summary="Create a new user")
def create_user(user: user_schema.UserRegister = Body(...)):
    return user_service.create_user(user)

@user_route.put('/user/{id}/')
def update_user(id: int, user: user_schema.UserBase):
    session.query(User).filter(
        User.id == id
    ).update(
        {
            User.username: user.username,
            User.email: user.email,
        }
    )
    session.commit()
    return "update user"

@user_route.delete('/user/{id}/', status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    session.query(User).filter(
        User.id == id
    ).delete()
    session.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@login_route.post(
    '/login',
    response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")