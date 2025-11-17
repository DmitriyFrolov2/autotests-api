
from  pydantic import BaseModel ,Field, EmailStr


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool = Field(alias="isActive")


user_data = {"id":1,"name":"Aliicee","email": "test@gmail.com","isActive": True}

user = User(**user_data)


class Car(BaseModel):
    numbers: int
    name: str
    id: int
    email: EmailStr

car = Car(numbers=3,name="Audi", id=455,email="test@yandex.ru")
print(car.numbers)



