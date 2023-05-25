from pydantic import BaseModel, constr


class SignUp(BaseModel):
    id: constr(min_length=8, max_length=11)
    nickname: constr(min_length=8, max_length=11)
    password: constr(min_length=6, max_length=20)


class Login(BaseModel):
    id: constr(min_length=8, max_length=11)
    password: constr(min_length=6, max_length=20)


class Certification(BaseModel):
    certificate: constr(min_length=1, max_length=255)
