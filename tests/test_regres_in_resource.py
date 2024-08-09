import requests
from jsonschema import validate
import json
import allure


endpoint_resource = '/unknown/'


@allure.feature("Получение данных о товаре")
@allure.story("Получение данных об одном товаре")
@allure.title("Получение данных о существующем товаре")
def test_get_single_resource(base_url):
    with allure.step('Отправление запроса'):
        id_user = 4
        response = requests.get(base_url + endpoint_resource + str(id_user))

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['data']['id'] == id_user

    with allure.step('Проверка схемы'):
        with open('schemas/resource.json') as file:
            schema = json.load(file)
        validate(response.json(), schema)


@allure.feature("Получение данных о товаре")
@allure.story("Получение данных об одном товаре")
@allure.title("Проверка ошибки при получении данных о несуществующем товаре")
def test_get_single_resource_not_found(base_url):
    with allure.step('Отправление запроса'):
        id_user = 45
        response = requests.get(base_url + endpoint_resource + str(id_user))

    with allure.step('Проверка кода'):
        assert response.status_code == 404

    with allure.step('Проверка ответа'):
        assert response.json() == {}
