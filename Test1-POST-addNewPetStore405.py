import pytest
import requests

def addNewPetStoreResponse405():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 9,
        'category': {
            'id': 7,
            'name': 'Ролик',
        },
        'name': 'doggie',
        'photoUrls': [
            'https://avatars.mds.yandex.net/i?id=18fbe6ed28d5b2484d957e22230a4198_l-4341820-images-thumbs&n=13',
        ],
        'tags': [
            {
                'id': 7,
                'name': 'Ролик',
            },
        ],
        'status': 'available',
    }

    return requests.get('https://petstore.swagger.io/v2/pet', headers=headers, json=json_data).status_code

def test():
    r = addNewPetStoreResponse405()
    assert r == 405