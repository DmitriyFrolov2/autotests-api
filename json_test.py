from jsonschema import validate, ValidationError

# Пример схемы
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

# Пример данных
data = {
  "name": "John Doe",
  "age": 30
}

try:
    validate(instance=data, schema=schema)
    print("Данные соответствуют схеме.")
except ValidationError as e:
    print(f"Ошибка валидации: {e.message}")


import json

from clients.authentication.authentication_schema import TokenSchema

Token_model = TokenSchema.model_json_schema()
print(json.dumps(Token_model,indent=2))

var = {"type":  "object",  "properties":  {"username":  {"type":  "string",  "minLength":  5,"maxLength":  15}},  "required":  ["username"]}

var2 = {
  "type": "object",
  "properties": {
    "username": {
      "type": "string",
      "minLength": 5,
      "maxLength": 15
    }
  },
  "required": ["username"]
}
