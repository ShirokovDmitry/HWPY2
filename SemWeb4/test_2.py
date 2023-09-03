import requests
import logging
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    adress_post = testdata['address_posts']


def my_posts(token):
    logging.debug('Open posts page')
    g = requests.get(adress_post, headers={'X-Auth-Token': token})
    if g and g.json() and g.json()['data']:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('page not available')


def not_my_posts(token):
    logging.debug('Open posts page')
    g = requests.get(adress_post, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    if g:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('page not available')


def createpost(token):
    logging.debug('Create new post')
    p = requests.post(adress_post, headers={'X-Auth-Token': token}, data={'title': 'New content',
                            'description': 'New description',
                            'content': 'A content'})
    if p:
        return p.json()
    else:
        logging.error('post not add')


def test_1(user_login, not_my_post):
    assert not_my_post in not_my_posts(user_login), "Test 1 Fail"


def test_2(user_login, my_post):
    createpost(user_login)
    assert my_post in my_posts(user_login), "Test 2 Fail"
