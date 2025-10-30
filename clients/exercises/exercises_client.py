from httpx import Response, QueryParams
from typing import TypedDict

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса для получения заданий определённого курса.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса для создания задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления данных задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с API заданий.
    Содержит методы для получения, создания, обновления и удаления заданий.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Выполняет получение списка заданий для определённого курса.

        :param query: Словарь с идентификатором курса (courseId).
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get("/api/v1/exercises", params=QueryParams(**query))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет получение информации о задании по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создаёт новое задание.

        :param request: Словарь с данными нового задания.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет данные существующего задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с обновлёнными данными.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
