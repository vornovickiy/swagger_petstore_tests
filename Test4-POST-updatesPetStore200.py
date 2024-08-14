import pytest
import requests

def updatesPetStoreResponse200():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'name': 'Кролик',
        'status': 'available',
    }

    return requests.post('https://petstore.swagger.io/v2/pet/9', headers=headers, data=data).status_code

def test():
        r = updatesPetStoreResponse200()
        assert r == 200