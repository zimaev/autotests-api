from clients.api_client import APIClient
from httpx import Response

from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str


class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str


class CreateFileResponse(TypedDict):
    file: File


class FilesClient(APIClient):

    def get_files_api(self, file_id: str) -> Response:
        return self.get(url=f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        return self.post("/api/v1/files",
                         data=request,
                         files={"upload_file": open(request["upload_file"], "rb")}
                         )

    def delete_dile_api(self, file_id: str) -> Response:
        return self.delete(url=f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponse:
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    return FilesClient(get_private_http_client(user))
