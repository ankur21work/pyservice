import pytest
from fastapi.testclient import TestClient
import allure
from service import *



@allure.feature("Allure Test")
@allure.story("Basic")
def test_read_root():
    assert True
