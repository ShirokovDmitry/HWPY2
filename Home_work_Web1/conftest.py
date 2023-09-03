import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()


@pytest.fixture()
def correct_word():
    return 'молоко'


@pytest.fixture()
def incorrect_word():
    return 'малако'


@pytest.fixture()
def user_login():
    rest1 = S.post(url=address, data={'username': username, 'password': password})
    return rest1.json()['token']


@pytest.fixture()
def post_title():
    return '999'


@pytest.fixture()
def post_title_new():
    return 'New Post'


@pytest.fixture()
def post_description():
    return 'A description'


@pytest.fixture()
def post_content():
    return 'Some content'


@pytest.fixture()
def create_post(user_login, post_title_new, post_description, post_content):
    rest2 = S.post(url=data['address_posts'], headers={'X-Auth-Token': user_login},
                   data={'title': post_title_new, 'description': post_description, 'content': post_content})
    return rest2.json()
