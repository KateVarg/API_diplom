import requests
import json
from jsonschema import validate
import allure
from path import project_root
import os


endpoint_register = '/register'


@allure.feature("Регистрация пользователя")
@allure.story("Регистрация нового пользователя")
@allure.title("Успешная регистрация нового пользователя")
def test_post_register_success(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post(base_url + endpoint_register, data=payload)

    with allure.step('Проверка кода'):
       assert response.status_code == 200

    with allure.step('Проверка схемы'):
        schema_path = os.path.join(project_root, 'schemas', 'register.json')
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
        response = requests.post(base_url + endpoint_register, data=payload)

    with allure.step('Проверка кода'):
        assert response.status_code == 400

    with allure.step('Проверка текста ошибки'):
        assert response.json()['error'] == "Missing password"
