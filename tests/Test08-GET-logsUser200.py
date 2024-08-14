import pytest
import requests

def logsUserResponse200():
    headers = {
        'accept': 'application/json',
    }

    params = {
        'username': 'krokus',
        'password': '1234567890',
    }

    return requests.get('https://petstore.swagger.io/v2/user/login', params=params, headers=headers).status_code

def test():
        r = logsUserResponse200()
        assert r == 200
