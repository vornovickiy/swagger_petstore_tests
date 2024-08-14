import pytest
import requests

def logsUserResponse400():
    headers = {
        'accept': 'application/json',
    }

    params = {
        'username': '?????????????????????&&&&&&&&&&&&&&&&&&',
        'password': '---------------------------------',
    }

    return requests.get('https://petstore.swagger.io/v2/user/login', params=params, headers=headers).status_code

def test():
        r = logsUserResponse400()
        assert r == 400
