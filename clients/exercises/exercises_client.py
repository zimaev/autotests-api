from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class GetExercisesQueryDict(TypedDict):
    """
    Словарь с courseId.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExerciseResponseDict(TypedDict):
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Обновления данных задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, request: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(request)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, request: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(request)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> ExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> ExerciseResponseDict:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """

        Удаление задания.
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(get_private_http_client(user))
