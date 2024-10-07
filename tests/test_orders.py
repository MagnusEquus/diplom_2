import requests
import data
import allure


class TestOrder:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Создаем пользователя, создаем заказ с его токеном. Проверяем сообщение и код ответа')
    def test_create_order_auth(self, user):
        payload = {
            "ingredients": data.BURGER_INGREDIENTS
        }
        token = user['token']
        response = requests.post(data.URL_ORDER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()["order"]["ingredients"][0]["_id"] == data.BURGER_INGREDIENTS[0]

    @allure.title('Создание заказа без авторизации')
    @allure.description('Создаем заказ, не передаем токен. Проверяем сообщение и код ответа')
    def test_create_order_no_auth(self):
        payload = {
            "ingredients": data.BURGER_INGREDIENTS
        }
        response = requests.post(data.URL_ORDER, data=payload)
        assert response.status_code == 200 and data.BURGER_NAME in response.json()["name"]

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Создаем заказ, но не передаем ингредиенты. Проверяем сообщение и код ответа')
    def test_no_ingredients(self):
        response = requests.post(data.URL_ORDER)
        assert response.status_code == 400 and response.json()["message"] == data.RESPONSE_ORDER_NO_INGREDIENTS

    @allure.title('Создание с неверными ингредиентами')
    @allure.description('Создаем заказ, передаем ингредиенты с неверными айди. Проверяем сообщение и код ответа')
    def test_wrong_ingredients(self):
        payload = {
            "ingredients": data.BURGER_WRONG_INGREDIENTS
        }
        response = requests.post(data.URL_ORDER, data=payload)
        assert response.status_code == 400 and response.json()["message"] == data.RESPONSE_ORDER_WRONG_INGREDIENTS
