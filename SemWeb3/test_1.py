import yaml

from testpage import OperationsHelper
from post_page import OperationAddPost
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
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f"Hello, {login}", 'test2 failed'


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationAddPost(browser)
    testpage.add_post()
    title1 = 'New title'
    testpage.post_context(title=title1, description='New description', content='New cotnent')
    res = testpage.check_post()
    assert res == title1, 'test3 failed'

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    title1 = 'New title2'
    testpage.post_context(title=title1, description='New description')
    res = testpage.check_post()
    assert res == title1, 'test4 failed'

def test_step5(browser):
    logging.info("Test5 Starting")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    title1 = 'New title3'
    testpage.post_context(title=title1, content='New cotnent')
    res = testpage.check_post()
    assert res == title1, 'test4 failed'

# def test_step2(x_selector_1, x_selector_2, btn_selector, x_selector_4, expected_result_2):
#     input1 = site.find_element('xpath', x_selector_1)
#     input1.clear()
#     input1.send_keys(testdata['username'])
#     input2 = site.find_element('xpath', x_selector_2)
#     input2.clear()
#     input2.send_keys(testdata['password'])
#     btn_selector = 'button'
#     btn = site.find_element('css', btn_selector)
#     btn.click()
#     link1 = site.find_element('xpath', x_selector_4)
#     result = link1.text
#     # site.close()
#     assert result == expected_result_2, 'test2 failed'
#
#
# def test_step3(btn_selector2, x_selector_5, x_selector_6, x_selector_7, btn_selector3, x_selector_8, expected_result_3):
#     btn_selector2 = 'button'
#     btn = site.find_element('css', btn_selector2)
#     btn.click()
#     time.sleep(3)
#     input1 = site.find_element('xpath', x_selector_5)
#     input1.clear()
#     input1.send_keys(testdata['title'])
#     input2 = site.find_element('xpath', x_selector_6)
#     input2.clear()
#     input2.send_keys(testdata['description'])
#     input3 = site.find_element('xpath', x_selector_7)
#     input3.clear()
#     input3.send_keys(testdata['content'])
#     btn_selector3 = 'button'
#     btn3 = site.find_element('css', btn_selector3)
#     btn3.click()
#     time.sleep(3)
#     link1 = site.find_element('xpath', x_selector_8)
#     result = link1.text
#     site.close()
#     assert result == expected_result_3, 'test3 failed'
