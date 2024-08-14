import json
from jsonschema import validate
import re
import allure
from reqresin_project_tests.utils import path
from reqresin_project_tests.utils.requests_helper import api_request


@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя")
@allure.title("Успешная авторизация пользователя")
def test_post_login_success(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        url = base_url
        response = api_request(url, endpoint="/login", method="POST", data=payload)
        token = response.json().get("token")
        token_pattern = r"^[A-Za-z0-9]+$"

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка токена'):
        assert re.match(token_pattern, token)

    with allure.step('Проверка схемы'):
        schema_path = path.abs_path_from_project('schemas/login.json')
        with open(schema_path) as file:
            schema = json.load(file)
        validate(response.json(), schema)


@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя")
@allure.title("Неуспешная авторизация пользователя")
def test_post_login_fail(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "peter@klaven"
        }
        url = base_url
        response = api_request(url, endpoint="/login", method="POST", data=payload)

    with allure.step('Проверка кода'):
        assert response.status_code == 400

    with allure.step('Проверка текста ошибки'):
        assert response.json()['error'] == "Missing password"
