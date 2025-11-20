from typing import Optional

from pydantic import BaseModel, ConfigDict, Field



class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: Optional[int] = Field(alias="maxScore")  # Обязательное, но может быть null
    min_score: Optional[int] = Field(alias="minScore")  # Обязательное, но может быть null
    order_index: Optional[int] = Field(alias="orderIndex", default=None)  # Необязательное
    description: str
    estimated_time: Optional[str] = Field(alias="estimatedTime")  # Обязательное, но может быть null



class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении одного задания.
    """
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    """
    Структура ответа при создании задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Структура ответа при обновлении задания.
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса для получения заданий определённого курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: Optional[int] = Field(alias="maxScore")  # Обязательное, но может быть null
    min_score: Optional[int] = Field(alias="minScore")  # Обязательное, но может быть null
    order_index: int = Field(alias="orderIndex",default=0)
    description: str
    estimated_time: Optional[str] = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления данных задания.
    """
    title: Optional[str] = Field(default=None)
    max_score: Optional[int] = Field(alias="maxScore", default=None)
    min_score: Optional[int] = Field(alias="minScore", default=None)
    order_index: Optional[int] = Field(alias="orderIndex",default=None)
    description: Optional[str] = Field(default=None)
    estimated_time: Optional[str] = Field(alias="estimatedTime", default=None)