import httpx
import json

# Отправка POST-запроса для получения токена
login_payload = {
    "email": "user@gmail.com",
    "password": "qwerty"
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)

print(f"Status Code: {login_response.status_code}")
print("Response JSON:")
print(json.dumps(login_response.json(), indent=2))

# Получаем accessToken из ответа
response_data = login_response.json()
access_token = response_data['token']['accessToken']

# Отправка GET-запроса с токеном
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = httpx.get(
    "http://localhost:8000/api/v1/users/me",
    headers=headers
)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=2))
