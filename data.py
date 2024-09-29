URL = "https://stellarburgers.nomoreparties.site/api/"
url_register = URL + "auth/register"
url_user = URL + "auth/user"
url_login = URL + "auth/login"
url_order = URL + "orders"

response_register_success = True
response_register_already_exists = "User already exists"
response_register_need_more = "Email, password and name are required fields"
response_login_success = True
response_login_incorrect = "email or password are incorrect"
response_user_not_authorized = "You should be authorised"
response_order_no_ingredients = "Ingredient ids must be provided"
response_order_wrong_ingredients = "One or more ids provided are incorrect"
response_get_orders_no_auth = "You should be authorised"

name = "test1"
password = "1test"
email = "magnusequus@yandex.ru"

burger_ingredients = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
burger_wrong_ingredients = ["11c0c5a71d1f82001bdaaa6f", "12c0c5a71d1f82001bdaaa70"]
burger_name = "Бессмертный метеоритный бургер"