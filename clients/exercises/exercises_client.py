from httpx import Response, QueryParams
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None



class GetExerciseResponse(TypedDict):
    """
    Описание структуры ответа при получении одного задания.
    """
    exercise: Exercise

class CreateExerciseResponse(TypedDict):
    """
    Структура ответа при создании задания.
    """
    exercise: Exercise

class UpdateExerciseResponse(TypedDict):
    """
    Структура ответа при обновлении задания.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при получении списка заданий.
    """
    exercises: list[Exercise]


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
        """
        return self.get("/api/v1/exercises", params=QueryParams(**query))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет получение информации о задании по его идентификатору.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создаёт новое задание.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет данные существующего задания.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # ----------- Методы верхнего уровня -----------

    def get_exercise(self, exercise_id: str) -> GetExerciseResponse:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponse:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponse:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным приватным HTTP-клиентом.
    """
    return ExercisesClient(client=get_private_http_client(user))
