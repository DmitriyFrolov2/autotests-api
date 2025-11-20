from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercies_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с API заданий.
    Содержит методы для получения, создания, обновления и удаления заданий.
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет получение списка заданий для определённого курса.
        """
        params = query.model_dump(by_alias=True, exclude_unset=True)
        return self.get("/api/v1/exercises", params=params)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет получение информации о задании по его идентификатору.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создаёт новое задание.
        """
        payload = request.model_dump(
            by_alias=True,
            exclude_unset=True,
            exclude_none=False
        )
        return self.post("/api/v1/exercises", json=payload)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновляет данные существующего задания.
        """
        payload = request.model_dump(
            by_alias=True,
            exclude_unset=True,
            exclude_none=True
        )
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=payload)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным приватным HTTP-клиентом.
    """
    return ExercisesClient(client=get_private_http_client(user))
