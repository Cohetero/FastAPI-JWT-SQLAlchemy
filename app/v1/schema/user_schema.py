from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example = "correo@email.com"
    )
    username: str = Field (
        ...,
        min_length = 3,
        max_length = 50,
        example = "Username"
    )

class User(UserBase):
    id: int = Field(
        ...,
        example = "5"
    )

class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length = 5,
        max_length = 64,
        example = "mypassword"
    )
