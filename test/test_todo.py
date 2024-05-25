import requests
import pytest

import utils.helepers as h

ENDPOINT = 'https://petstore.swagger.io/v2'

class C:
    def f(self):
        return 1

@pytest.fixture
def setup_teardown():
    print("Set up")
    yield
    print('Tear Down')

@pytest.fixture
def c_instance():
    return C()


def test_create_pet():
    payload={
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
            },
        "name": "doggie",
        "photoUrls": [
            "string"
            ],
        "tags": [
            {
                "id": 0,
                "name": "string"
                }
            ],
        "status": "available"
        }
    
    post_response = requests.post(ENDPOINT+"/pet",json=payload)
    
    id = post_response.json()["id"]

    print('This is message from the first tests')
    h.print_word('Hello there!')

    assert post_response.status_code == 200
    
    get_response = requests.get(f"{ENDPOINT}/pet/{id}")
    assert get_response.status_code == 200

@pytest.mark.usefixtures('setup_teardown')
def test_func1():
    print("This is error message from second test")
    assert True

def test_func2(c_instance):
    print("This is error message from second test")
    assert c_instance.f() == 1