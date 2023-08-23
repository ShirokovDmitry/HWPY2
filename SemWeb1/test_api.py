import yaml

from task1 import check_text
import requests
import yaml

S = requests.Session()
with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address_posts']


def test_step1(correct_word, incorrect_word):
    assert correct_word in check_text(incorrect_word), 'Test1 Failed'


def test_rest(user_login, post_title):
    res = S.get(url=address, headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()['data']
    r = [i['title'] for i in res]
    assert post_title in r, 'Test rest Failed'
