import pytest
import requests

def findsPetsStatusResponse400():
    headers = {
        'accept': 'application/json',
    }

    params = {
        'status': 'occupied',
    }

    return requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers).status_code

def test():
        r = findsPetsStatusResponse400()
        assert r == 400