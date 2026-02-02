from _pytest.fixtures import SubRequest
import pytest


@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])  # Параметризируем по хосту
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0  # Проверка указана для примера



@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# Фикстура будет возвращать три разных хоста
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    # Внутри атрибута param находится одно из значений "https://dev.company.com",
    # "https://stable.company.com", "https://prod.company.com"
    return request.param


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # Используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"Running test on host: {host}")

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


