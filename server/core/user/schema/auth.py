from pydantic import BaseModel, constr, Field
from typing import Union


class SignUp(BaseModel):
    id: constr(min_length=8, max_length=11)
    nickname: constr(min_length=8, max_length=11)
    password: constr(min_length=6, max_length=20)


class Login(BaseModel):
    id: constr(min_length=8, max_length=11)
    password: constr(min_length=6, max_length=20)


class Certification(BaseModel):
    certificate: constr(min_length=1, max_length=255)


class Profile(BaseModel):
    profile: Union[str, None]
    nickname: Union[str, None]
    introduce: Union[str, None]
