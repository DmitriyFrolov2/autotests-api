from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    CreateCourseRequestSchema,
    UpdateCourseRequestSchema,
    CreateCourseResponseSchema,
    CourseSchema
)

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        params = query.model_dump(by_alias=True, exclude_unset=True)
        return self.get("/api/v1/courses", params=params)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:

        payload = request.model_dump(
            by_alias=True,
            exclude_unset=True,
            exclude_none=False
        )
        return self.post("/api/v1/courses", json=payload)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:

        payload = request.model_dump(
            by_alias=True,
            exclude_unset=True,
            exclude_none=True
        )

        return self.patch(f"/api/v1/courses/{course_id}", json=payload)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод создания курса с валидацией ответа.
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def get_course(self, course_id: str) -> CourseSchema:
        """
        Метод получения курса с валидацией ответа.
        """
        response = self.get_course_api(course_id)
        return CourseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
