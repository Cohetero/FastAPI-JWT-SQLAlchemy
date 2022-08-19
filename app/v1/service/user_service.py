from fastapi import HTTPException, status
from app.v1.model.user_model import User as User_Model
from app.v1.schema import user_schema
from .auth_service import get_password_hash
from app.v1.utils.db import Session

session = Session()

def create_user(user: user_schema.UserRegister):
    get_user = session.query(User_Model).filter((User_Model.email == user.email) | (User_Model.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = msg
        )
    db_user = User_Model(
        username = user.username,
        email = user.email,
        password = get_password_hash(user.password)
    )

    session.add(db_user)
    session.commit()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )