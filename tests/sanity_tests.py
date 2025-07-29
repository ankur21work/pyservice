import pytest
from fastapi.testclient import TestClient
import allure
from service import *

client = TestClient(app)

@allure.feature("Root")
@allure.story("GET /")
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

@allure.feature("Item")
@allure.story("POST /items/")
@pytest.mark.parametrize("name,value", [("foo", 123), ("bar", 456)])
def test_create_item(name, value):
    with allure.step(f"Creating item {name} with value {value}"):
        response = client.post("/items/", json={"name": name, "value": value})
        assert response.status_code == 200
        assert response.json() == {"item_name": name, "item_value": value}