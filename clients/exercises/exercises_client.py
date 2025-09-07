from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, \
    CreateExerciseRequestSchema, UpdateExerciseRequestSchema, ExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, request: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(request)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, request: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(request)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание задания.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> ExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """

        Удаление задания.
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(get_private_http_client(user))
