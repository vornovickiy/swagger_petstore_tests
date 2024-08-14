import pytest
import requests

def findsPetsStatusResponse200():
    headers = {
        'accept': 'application/json',
    }

    params = {
        'status': 'available',
    }

    return requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers).status_code

def test():
        r = findsPetsStatusResponse200()
        assert r == 200