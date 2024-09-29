import requests
import data
import helpers
import allure


class TestCreate:

    @allure.title('Создание юзера')
    @allure.description('Создаем нового юзера по данным из data, проверяем код и сообщение ответа. После и вначале теста удаляем')
    def test_create_positive(self):
        helpers.delete_user(data.email, data.password)
        payload = {
            "email": data.email,
            "password": data.password,
            "name": data.name
        }
        response = requests.post(data.url_register, data=payload)
        assert response.json()["success"] == data.response_register_success and response.status_code == 200
        helpers.delete_user(data.email, data.password)

    @allure.title('Создание уже существующего юзера')
    @allure.description('Создаем юзера с уже существующими кредами. Проверяем сообщение и код ответа')
    def test_create_existing(self, user):
        response = requests.post(data.url_register, data=user)
        assert response.json()["message"] == data.response_register_already_exists and response.status_code == 403

    @allure.title('Недостаточные данные')
    @allure.description('Создаем нового юзера нодаем недостаточно данных. Проверяем сообщение и код ответа')
    def test_create_need_more(self):
        helpers.delete_user(data.email, data.password)
        payload = {
            "email": data.email,
            "name": data.name
        }
        response = requests.post(data.url_register, data=payload)
        assert response.json()["message"] == data.response_register_need_more and response.status_code == 403
