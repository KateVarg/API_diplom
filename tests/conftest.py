import pytest
import requests

from API_autotest_diplom.utils import attach


@pytest.fixture()
def base_url():
    base_url = 'https://reqres.in/api'

    return base_url
