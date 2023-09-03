import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_log import send_to_email

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']
    login_n = testdata['username']
    password = testdata['password']
    adress_post = testdata['adress_post']



@pytest.fixture(scope="session")
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    send_to_email()
    driver.quit()

@pytest.fixture()
def user_login():
    r = requests.post(adress_post, data={'username': login_n, 'password': password})
    return r.json()['token']


@pytest.fixture()
def not_my_post():
    return 'укпукп'


@pytest.fixture()
def my_post():
    return 'New content'