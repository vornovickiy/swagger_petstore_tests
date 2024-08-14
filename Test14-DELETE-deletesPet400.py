import pytest
import requests

def deletesPetResponse400():
    headers = {
        'accept': 'application/json',
        'api_key': ')))))))))((((((((((((',
    }

    return requests.delete('https://petstore.swagger.io/v2/pet/9', headers=headers).status_code

def test():
        r = deletesPetResponse400()
        assert r == 400
