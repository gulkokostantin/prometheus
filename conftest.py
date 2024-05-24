import pytest
from modules.api.clients.github import GitHub


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Kostiantyn"
        self.second_name = "Gulko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    # Створити об'єкт класу User
    user = User()
    # Викликати метод об'єкту create
    user.create()
    # Повернути об'єкт після виклику методу об'єкту create в тести
    yield user
    # Після виконання тесту викликати метод об'єкту remove
    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api
