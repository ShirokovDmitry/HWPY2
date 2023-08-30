import yaml

from testpage import OperationsHelper
from post_page import OperationAddPost
from contact_page import ConatctPage
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

    login = testdata['username']
    password = testdata['password']


# def test_step1(browser):
#     logging.info("Test1 Starting")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login("test")
#     testpage.enter_pass("test")
#     testpage.click_login_button()
#     assert testpage.get_error_text() == "401", 'test1 failed'


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f"Hello, {login}", 'test2 failed'

def test_contact(browser):
    logging.info("testContact Starting")
    testpage = ConatctPage(browser)
    testpage.contact_enter()
    txt = 'Form successfully submitted'
    testpage.post_contact(name='A name', email='Aemail@email.em', content='New content')
    alert = testpage.switch_page()
    assert alert.text == txt, 'testCont failed'



# def test_step3(browser):
#     logging.info("Test3 Starting")
#     testpage = OperationAddPost(browser)
#     testpage.add_post()
#     title1 = 'New title'
#     testpage.post_context(title=title1, description='New description', content='New cotnent')
#     res = testpage.check_post()
#     assert res == title1, 'test3 failed'
#
# def test_step4(browser):
#     logging.info("Test4 Starting")
#     testpage = OperationAddPost(browser)
#     testpage.go_to_site()
#     testpage.add_post()
#     title1 = 'New title2'
#     testpage.post_context(title=title1, description='New description')
#     res = testpage.check_post()
#     assert res == title1, 'test4 failed'
#
# def test_step5(browser):
#     logging.info("Test5 Starting")
#     testpage = OperationAddPost(browser)
#     testpage.go_to_site()
#     testpage.add_post()
#     title1 = 'New title3'
#     testpage.post_context(title=title1, content='New cotnent')
#     res = testpage.check_post()
#     assert res == title1, 'test4 failed'
