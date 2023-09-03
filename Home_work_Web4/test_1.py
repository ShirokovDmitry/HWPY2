import time
import yaml
from testpage import OperationsHelper
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    login = testdata['username']
    password = testdata['password']



def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", 'test1 failed'


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f"Hello, {login}", 'test2 failed'


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.add_post()
    title1 = 'New title'
    testpage.enter_title(title1)
    testpage.enter_description('New description')
    testpage.enter_content('New content')
    testpage.create_post()
    time.sleep(1)
    res = testpage.check_post()
    assert res == title1, 'test3 failed'

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.add_post()
    title1 = 'New title2'
    testpage.enter_title(title1)
    testpage.enter_description('New description')
    testpage.create_post()
    time.sleep(1)
    res = testpage.check_post()
    assert res == title1, 'test4 failed'
#
def test_step5(browser):
    logging.info("Test5 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.add_post()
    title1 = 'New title3'
    testpage.enter_title(title1)
    testpage.enter_content('New content')
    testpage.create_post()
    time.sleep(1)
    res = testpage.check_post()
    assert res == title1, 'test4 failed'

def test_contact(browser):
    logging.info("testContact Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.contact_enter()
    txt = 'Form successfully submitted'
    testpage.enter_name('A name')
    testpage.enter_email('Aemail@email.em')
    testpage.enter_content_cont('New content')
    testpage.contact_btn()
    time.sleep(1)
    alert = testpage.switch_page()
    assert alert.text == txt, 'testCont failed'

