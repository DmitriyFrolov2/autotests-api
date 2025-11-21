from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from clients.users.users_schema import (
    CreateUserRequestSchema,
    GetUserResponseSchema
)

# Инициализируем PublicUsersClient
public_users_client = get_public_users_client()

# Формируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Создаём пользователя
create_user_response = public_users_client.create_user(create_user_request)

# ID созданного пользователя
user_id = create_user_response.user.id

# Подготовка данных для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализируем PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Выполняем GET /api/v1/users/{user_id}
get_user_response = private_users_client.get_user_api(user_id)

# Генерируем JSON Schema от модели ответа
get_user_schema = GetUserResponseSchema.model_json_schema()

# Валидируем JSON Schema
validate_json_schema(
    instance=get_user_response.json(),
    schema=get_user_schema
)

print(get_user_response.json())
print(get_user_schema)
