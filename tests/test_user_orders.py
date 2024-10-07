import requests
import data
import allure


class TestUserOrders:

    @allure.title('Получить заказы пользователя')
    @allure.description('Создаем пользователя, добавляем ему заказ. Получаем список с его заказами передав токен. Проверяем сообщение и код ответа')
    def test_get_user_orders_auth(self, user):
        payload = {
            "ingredients": data.BURGER_INGREDIENTS
        }
        token = user['token']
        response = requests.post(data.URL_ORDER, headers={'Authorization': token}, data=payload)
        order_id = response.json()["order"]["_id"]
        response = requests.get(data.URL_ORDER, headers={'Authorization': token})
        assert response.status_code == 200 and response.json()["orders"][0]["_id"] == order_id

    @allure.title('Получить заказыва пользователя без авторизации')
    @allure.description('Пытаемся получить заказы пользователя, не передав токен.ф Проверяем сообщение и код ответа')
    def test_get_user_orders_no_auth(self, user):
        response = requests.get(data.URL_ORDER)
        assert response.status_code == 401 and response.json()["message"] == data.RESPONSE_GET_ORDERS_NO_AUTH
