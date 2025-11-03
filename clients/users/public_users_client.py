from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
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

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет POST-запрос для создания пользователя
        :param request:Данные пользователя в виде словаря (email, password, lastName, firstName, middleName).
        :return:Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экзепляр PublicUsersClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())