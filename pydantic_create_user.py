from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """
     модель данных пользователя
    """
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    запрос на создание пользователя
    """
    email: str
    password: str
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    ответ с данными созданного пользователя
    """
    user: UserSchema
