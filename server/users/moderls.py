from pydantic import BaseModel

class Users(BaseModel):
    id:int
    login:str
    password:int

class InputUsers(BaseModel):
    login:str
    password:str

class UserGroup(BaseModel):
    id:int
    name:str


