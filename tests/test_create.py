import requests
import data
import helpers
import allure


class TestCreate:

    @allure.title('Создание юзера')
    @allure.description('Создаем нового юзера по данным из data, проверяем код и сообщение ответа. После и вначале теста удаляем')
    def test_create_positive(self):
        helpers.delete_user(data.EMAIL, data.PASSWORD)
        payload = {
            "email": data.EMAIL,
            "password": data.PASSWORD,
            "name": data.NAME
        }
        response = requests.post(data.URL_REGISTER, data=payload)
        assert response.json()["success"] == data.RESPONSE_REGISTER_SUCCESS and response.status_code == 200
        helpers.delete_user(data.EMAIL, data.PASSWORD)

    @allure.title('Создание уже существующего юзера')
    @allure.description('Создаем юзера с уже существующими кредами. Проверяем сообщение и код ответа')
    def test_create_existing(self, user):
        response = requests.post(data.URL_REGISTER, data=user)
        assert response.json()["message"] == data.RESPONSE_REGISTER_ALREADY_EXISTS and response.status_code == 403

    @allure.title('Недостаточные данные')
    @allure.description('Создаем нового юзера нодаем недостаточно данных. Проверяем сообщение и код ответа')
    def test_create_need_more(self):
        helpers.delete_user(data.EMAIL, data.PASSWORD)
        payload = {
            "email": data.EMAIL,
            "name": data.NAME
        }
        response = requests.post(data.URL_REGISTER, data=payload)
        assert response.json()["message"] == data.RESPONSE_REGISTER_NEED_MORE and response.status_code == 403
