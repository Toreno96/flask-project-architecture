import pydantic


class SchemaUserCreateInput(pydantic.BaseModel):
    email: str
    username: str


class SchemaUserCreateOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str


class SchemaUserListOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str


class SchemaUserDetailOutput(pydantic.BaseModel):
    id: int
    email: str
    username: str
