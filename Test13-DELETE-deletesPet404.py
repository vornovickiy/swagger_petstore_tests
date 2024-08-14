import pytest
import requests

def deletesPetResponse404():
    headers = {
        'accept': 'application/json',
        'api_key': 'special-key',
    }

    return requests.delete('https://petstore.swagger.io/v2/pet/99999999999999999', headers=headers).status_code

def test():
        r = deletesPetResponse404()
        assert r == 404
