import pytest
import requests

def updatedUserResponse200():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 11,
        'username': 'krokus',
        'firstName': 'Юрий',
        'lastName': 'Котов',
        'email': 'krokus1234567890@yandex.ru',
        'password': '1234567890',
        'phone': '+79055647733',
        'userStatus': 5,
    }

    return requests.put('https://petstore.swagger.io/v2/user/krokus', headers=headers, json=json_data).status_code

def test():
        r = updatedUserResponse200()
        assert r == 200
