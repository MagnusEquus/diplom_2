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
        response = requests.post(data.url_login, data=payload)
        assert response.json()["success"] == data.response_login_success and response.status_code == 200

    @allure.title('Логин с неверными данными')
    @allure.description('Фикстурой создаем пользователя, логинимся под неверными данными. Проверяем сообщение и код ответа')
    def test_login_negative(self, user):
        payload = {
            "email": "",
            "password": ""
        }
        response = requests.post(data.url_login, data=payload)
        assert response.json()["message"] == data.response_login_incorrect and response.status_code == 401