import pytest

@pytest.fixture
def clear_books():
    print("[FIXTURE] Удаляем все данные")

@pytest.fixture
def fill_books():
    print("[FIXTURE] создаем новые данные")

@pytest.mark.usefixtures('clear_books','fill_books')
class TestLibrary:
    def test_read_read(self, fill_books,clear_books):
        ...

    def test_delete_book(self):
        ...