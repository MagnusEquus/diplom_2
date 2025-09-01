import pytest
import data
import allure
import helpers


@allure.step('Создаем юзера, выдаем его креды и токен. После - удаляем')
@pytest.fixture
def user():
    helpers.delete_user(data.EMAIL, data.PASSWORD)
    helpers.register_user(data.EMAIL, data.PASSWORD, data.NAME)
    creds = {
        "email": data.EMAIL,
        "password": data.PASSWORD,
        "name": data.NAME,
        "token": helpers.get_user_token(data.EMAIL, data.PASSWORD)
    }
    yield creds
    helpers.delete_user(data.EMAIL, data.PASSWORD)

