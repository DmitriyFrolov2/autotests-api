
from tools.fakers import fake
from pydantic import BaseModel, ConfigDict, Field



class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")  # Обязательное, но может быть null
    min_score: int = Field(alias="minScore")  # Обязательное, но может быть null
    order_index: int = Field(alias="orderIndex")  # Необязательное
    description: str
    estimated_time: str = Field(alias="estimatedTime")  # Обязательное, но может быть null



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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore",default_factory=fake.max_score)  # Обязательное, но может быть null
    min_score: int = Field(alias="minScore",default_factory=fake.min_score)  # Обязательное, но может быть null
    order_index: int = Field(alias="orderIndex",default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления данных задания.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore",default_factory=fake.max_score)
    min_score: int = Field(alias="minScore",default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex",default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)