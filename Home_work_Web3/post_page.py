import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class AddPostLocators:
    LOCATOR_ADD_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DISCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_POST = (By.CSS_SELECTOR, """#create-item > div > div > div:nth-child(7) > div > button > span""")
    LOCATOR_CHECK_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")


class OperationAddPost(BasePage):
    def add_post(self):
        logging.info('Add post')
        add_post_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST)
        add_post_btn.click()

    def post_context(self, title=None, description=None, content=None):
        logging.info(f'fill post: {title}, {description}, {content}')
        title_field = self.find_element(AddPostLocators.LOCATOR_TITLE)
        if title:
            title_field.clear()
            title_field.send_keys(title)
        description_field = self.find_element(AddPostLocators.LOCATOR_DISCRIPTION)
        if description:
            description_field.clear()
            description_field.send_keys(description)
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTENT)
        if content:
            content_field.clear()
            content_field.send_keys(content)
        btn = self.find_element(AddPostLocators.LOCATOR_CREATE_POST)
        btn.click()

    def check_post(self):
        logging.info('checking new post')
        time.sleep(1)
        return self.find_element(AddPostLocators.LOCATOR_CHECK_POST).text
