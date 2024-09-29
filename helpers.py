import requests
import allure
import data


@allure.step('Создаем юзера с задаными данными')
def register_user(email, password, name):
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    requests.post(data.url_register, data=payload)


@allure.step('Удаляем юзера по почте и паролю')
def delete_user(email, password):
    token = get_user_token(email, password)
    requests.delete(data.url_user, headers={'Authorization': token})


@allure.step('Получаем токен юзера по почте и паролю')
def get_user_token(email, password):
    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(data.url_login, data=payload)
    if response.status_code != 401:
        token = response.json()["accessToken"]
        return token