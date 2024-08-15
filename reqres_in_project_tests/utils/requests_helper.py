from reqres_in_project_tests.utils.attach import response_logging, response_attaching
import requests


def api_request(base_url, endpoint, method, data=None, params=None):
    url = f"{base_url}{endpoint}"
    response = requests.request(method, url, data=data, params=params)
    response_logging(response)
    response_attaching(response)
    return response
