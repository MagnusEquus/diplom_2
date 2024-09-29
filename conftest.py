import pytest
import data
import allure
import helpers


@allure.step('Создаем юзера, выдаем его креды и токен. После - удаляем')
@pytest.fixture
def user():
    helpers.delete_user(data.email, data.password)
    helpers.register_user(data.email, data.password, data.name)
    creds = {
        "email": data.email,
        "password": data.password,
        "name": data.name,
        "token": helpers.get_user_token(data.email, data.password)
    }
    yield creds
    helpers.delete_user(data.email, data.password)

