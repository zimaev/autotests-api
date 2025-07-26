from clients.api_client import APIClient
from httpx import Response

from typing import TypedDict


class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str


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
