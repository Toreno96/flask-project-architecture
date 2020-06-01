import pydantic


class UserCreateInput(pydantic.BaseModel):
    email: str
    username: str


class UserCreateOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str


class UserListOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str


class UserDetailOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str
