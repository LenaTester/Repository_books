import pytest
import json

from pythonProject.Repository_books.data_generator import random_string
from pythonProject.Repository_books.api.token_api import TokenApi

@pytest.fixture
def token_generation():
    name = random_string()
    token_json = {'clientName': name, 'clientEmail': name+'@gmail.com'}
    token_python = json.dumps(token_json)
    return token_python

@pytest.fixture
def token_value(token_generation):
    response = TokenApi().post_token(token_generation)
    token_dict = response.json()
    token = token_dict['accessToken']
    return token

@pytest.fixture
def order_a_book():
    name = random_string()
    order_json = {'bookId': 1, 'customerName': name}
    order_python = json.dumps(order_json)
    return order_python

@pytest.fixture
def new_name():
    name = random_string()
    name_json = {'customerName': name}
    name_python = json.dumps(name_json)
    return name_python