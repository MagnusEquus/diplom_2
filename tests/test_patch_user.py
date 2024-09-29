import requests
import data
import helpers
import allure


class TestPatchUser:

    @allure.title('Обновление кредов пользователя')
    @allure.description('Создаем пользователя, меняем креды, передав токен. Смотрим что креды у юзера новые. Проверяем сообщение и код ответа')
    def test_patch_positive(self, user):
        token = user['token']
        new_email = 'magnusequus+123@yandex.ru'
        new_name = 'qwerty'
        helpers.delete_user(new_email, user['password'])
        payload = {
            "email": new_email,
            "name": new_name
        }
        response = requests.patch(data.url_user, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()["user"]["email"] == new_email and response.json()["user"]["name"] == new_name
        helpers.delete_user(new_email, user['password'])

    @allure.title('Смены кредов пользователя без авторизации')
    @allure.description('Создаем пользователя, пробуем поменять креды, но не передаем токен. Проверяем сообщение и код ответа')
    def test_patch_without_auth(self, user):
        payload = {
            "email": user['email'],
            "password": user['password']
        }
        response = requests.patch(data.url_user, data=payload)
        assert response.status_code == 401 and response.json()["message"] == data.response_user_not_authorized

