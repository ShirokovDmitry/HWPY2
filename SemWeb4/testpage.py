from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])




class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.info(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="pass form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word, description="title form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DISCRIPTION"], word, description="description form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="name form")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL"], word, description="email form")

    def enter_content_cont(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word, description="content_cont form")



    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")


    def add_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_POST"], description="add post")


    def contact_enter(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_PAGE"], description="contact")


    def create_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST"], description="create post")

    def contact_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")



    #   GET TEXT

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    # def get_user_text(self):
    #     user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
    #     text = user_field.text
    #     logging.info(f"We find {text} in user field {TestSearchLocators.LOCATOR_HELLO[1]}")
    #     return text

    def check_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_POST"])

    def auth(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_AUTH"])



    def switch_page(self):
        logging.info('switch contact')
        alert = self.driver.switch_to.alert
        return alert






















