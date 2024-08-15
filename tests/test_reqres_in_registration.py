import json
from jsonschema import validate
import allure
from reqres_in_project_tests.utils import path
from reqres_in_project_tests.utils.requests_helper import api_request


@allure.feature("Регистрация пользователя")
@allure.story("Регистрация нового пользователя")
@allure.title("Успешная регистрация нового пользователя")
def test_post_register_success(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        url = base_url
        response = api_request(url, endpoint="/register", method="POST", data=payload)

    with allure.step('Проверка кода'):
       assert response.status_code == 200

    with allure.step('Проверка схемы'):
        schema_path = path.abs_path_from_project('schemas/register.json')
        with open(schema_path) as file:
            schema = json.load(file)
        validate(response.json(), schema)


@allure.feature("Регистрация пользователя")
@allure.story("Регистрация нового пользователя")
@allure.title("Неуспешная регистрация нового пользователя")
def test_post_register_fail(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "sydney@fife"
        }
        url = base_url
        response = api_request(url, endpoint="/register", method="POST", data=payload)

    with allure.step('Проверка кода'):
        assert response.status_code == 400

    with allure.step('Проверка текста ошибки'):
        assert response.json()['error'] == "Missing password"
