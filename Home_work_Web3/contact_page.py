import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class AddPostLocators:
    LOCATOR_CONTACT_PAGE = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME = (By.XPATH,"""//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class ConatctPage(BasePage):
    def contact_enter(self):
        logging.info('enter contact')
        add_post_btn = self.find_element(AddPostLocators.LOCATOR_CONTACT_PAGE)
        add_post_btn.click()

    def post_contact(self, name=None, email=None, content=None):
        logging.info(f'fill contact: {name}, {email}, {content}')
        name_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_NAME)
        if name:
            name_field.clear()
            name_field.send_keys(name)
        email_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_EMAIL)
        if email:
            email_field.clear()
            email_field.send_keys(email)
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_CONTENT)
        if content:
            content_field.clear()
            content_field.send_keys(content)
        btn = self.find_element(AddPostLocators.LOCATOR_CONTACT_BTN)
        btn.click()
        time.sleep(1)

    def switch_page(self):
        logging.info('switch contact')
        alert = self.driver.switch_to.alert
        return alert
