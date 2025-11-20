from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


# Добавили описание структуры курса
class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: Optional[int] = Field(alias="maxScore", default=None)  # Может быть null
    min_score: Optional[int] = Field(alias="minScore", default=None)  # Может быть null
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: Optional[str] = Field(alias="estimatedTime", default=None)  # Может быть null
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: Optional[int] = Field(alias="maxScore")
    min_score: Optional[int] = Field(alias="minScore")
    description: str
    preview_file_id: str = Field(alias="previewFileId")
    estimated_time: Optional[str] = Field(alias="estimatedTime")
    created_by_user_id: str = Field(alias="createdByUserId")


# Добавили описание структуры ответа на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] = Field(alias="title",default=None)
    max_score: Optional[int] = Field(alias="maxScore",default=None)
    min_score: Optional[int] = Field(alias="minScore",default=None)
    description: Optional[str] = Field(alias="description",default=None)
    estimated_time: Optional[str] = Field(alias="estimatedTime",default=None)