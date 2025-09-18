from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры ответа на получение файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    # Добавили генерацию случайного названия файла с расширением PNG
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    file: FileSchema
