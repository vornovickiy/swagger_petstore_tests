import pytest
import requests

def updatedUserResponse404():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 777777777,
        'username': 'ggg',
        'firstName': 'fff',
        'lastName': 'fff',
        'email': 'fff@yandex.ru',
        'password': 'fff',
        'phone': 'fff',
        'userStatus': 555555555,
    }

    return requests.put('https://petstore.swagger.io/v2/user/ggggg', headers=headers, json=json_data).status_code

def test():
        r = updatedUserResponse404()
        assert r == 404
