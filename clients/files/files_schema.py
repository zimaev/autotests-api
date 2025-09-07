from pydantic import BaseModel, HttpUrl


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

    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    file: FileSchema
