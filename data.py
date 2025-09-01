URL = "https://stellarburgers.nomoreparties.site/api/"
URL_REGISTER = URL + "auth/register"
URL_USER = URL + "auth/user"
URL_LOGIN = URL + "auth/login"
URL_ORDER = URL + "orders"

RESPONSE_REGISTER_SUCCESS = True
RESPONSE_REGISTER_ALREADY_EXISTS = "User already exists"
RESPONSE_REGISTER_NEED_MORE = "Email, password and name are required fields"
RESPONSE_LOGIN_SUCCESS = True
RESPONSE_LOGIN_INCORRECT = "email or password are incorrect"
RESPONSE_USER_NOT_AUTHORIZED = "You should be authorised"
RESPONSE_ORDER_NO_INGREDIENTS = "Ingredient ids must be provided"
RESPONSE_ORDER_WRONG_INGREDIENTS = "One or more ids provided are incorrect"
RESPONSE_GET_ORDERS_NO_AUTH = "You should be authorised"

NAME = "test1"
PASSWORD = "1test"
EMAIL = "magnusequus@yandex.ru"

BURGER_INGREDIENTS = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
BURGER_WRONG_INGREDIENTS = ["11c0c5a71d1f82001bdaaa6f", "12c0c5a71d1f82001bdaaa70"]
BURGER_NAME = "Бессмертный метеоритный бургер"