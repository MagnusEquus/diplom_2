import requests
import data
import allure


class TestLogin:

    @allure.title('Успешный логин')
    @allure.description('Фикстурой создаем пользователя, логинимся под ним. Проверяем сообщение и код ответа')
    def test_login_positive(self, user):
        payload = {
            "email": user['email'],
            "password": user['password']
        }
        response = requests.post(data.URL_LOGIN, data=payload)
        assert response.json()["success"] == data.RESPONSE_LOGIN_SUCCESS and response.status_code == 200

    @allure.title('Логин с неверными данными')
    @allure.description('Фикстурой создаем пользователя, логинимся под неверными данными. Проверяем сообщение и код ответа')
    def test_login_negative(self, user):
        payload = {
            "email": "",
            "password": ""
        }
        response = requests.post(data.URL_LOGIN, data=payload)
        assert response.json()["message"] == data.RESPONSE_LOGIN_INCORRECT and response.status_code == 401