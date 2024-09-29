import requests
import data
import allure


class TestOrder:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Создаем пользователя, создаем заказ с его токеном. Проверяем сообщение и код ответа')
    def test_create_order_auth(self, user):
        payload = {
            "ingredients": data.burger_ingredients
        }
        token = user['token']
        response = requests.post(data.url_order, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()["order"]["ingredients"][0]["_id"] == data.burger_ingredients[0]

    @allure.title('Создание заказа без авторизации')
    @allure.description('Создаем заказ, не передаем токен. Проверяем сообщение и код ответа')
    def test_create_order_no_auth(self):
        payload = {
            "ingredients": data.burger_ingredients
        }
        response = requests.post(data.url_order, data=payload)
        assert response.status_code == 200 and data.burger_name in response.json()["name"]

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Создаем заказ, но не передаем ингредиенты. Проверяем сообщение и код ответа')
    def test_no_ingredients(self):
        response = requests.post(data.url_order)
        assert response.status_code == 400 and response.json()["message"] == data.response_order_no_ingredients

    @allure.title('Создание с неверными ингредиентами')
    @allure.description('Создаем заказ, передаем ингредиенты с неверными айди. Проверяем сообщение и код ответа')
    def test_wrong_ingredients(self):
        payload = {
            "ingredients": data.burger_wrong_ingredients
        }
        response = requests.post(data.url_order, data=payload)
        assert response.status_code == 400 and response.json()["message"] == data.response_order_wrong_ingredients
