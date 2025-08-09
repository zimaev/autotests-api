from clients.api_client import APIClient
from httpx import Response

from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class File(TypedDict):
    """
    Описание структуры ответа на получение файла.
    """
    id: str
    filename: str
    directory: str
    url: str


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str
    directory: str
    upload_file: str


class CreateFileResponse(TypedDict):
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_files_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/files",
                         data=request,
                         files={"upload_file": open(request["upload_file"], "rb")}
                         )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.delete(url=f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponse:
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """

    return FilesClient(get_private_http_client(user))
