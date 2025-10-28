from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Структура тела POST-запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для взаимодействия с /api/v1/users.

    Используется для выполнения запросов, не требующих авторизации
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод выполняет POST-запрос для создания пользователя
        :param request:Данные пользователя в виде словаря (email, password, lastName, firstName, middleName).
        :return:Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request)
