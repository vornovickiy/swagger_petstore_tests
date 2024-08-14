import pytest
import requests

def deleteUserResponse404():
    headers = {
        'accept': 'application/json',
    }

    return requests.delete('https://petstore.swagger.io/v2/user/hhhhhhh', headers=headers).status_code

def test():
        r = deleteUserResponse404()
        assert r == 404
