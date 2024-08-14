import pytest
import requests

def updatesPetStoreResponse405():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'name': 'Кролик',
        'status': 'available',
    }

    return requests.get('https://petstore.swagger.io/v2/pet/', headers=headers, data=data).status_code

def test():
        r = updatesPetStoreResponse405()
        assert r == 405