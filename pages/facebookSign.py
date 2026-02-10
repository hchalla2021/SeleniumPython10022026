from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
class FacebookSignPage(BasePage):
    name= (By.XPATH, "//input[@name='firstname']")
    mobile_number= (By.XPATH, "//input[@name='reg_email__']")
    password= (By.XPATH, "//input[@name='reg_passwd__']")
    day= (By.XPATH, "//select[@name='birthday_day']")

    def login_facebook(self, name, mobile_number, password):
        self.enter_text(self.name, name)
        time.sleep(5)
        self.enter_text(self.mobile_number, mobile_number)
        time.sleep(5)
        self.enter_text(self.password, password)
        time.sleep(5)
    def select_day(self, day):
        time.sleep(5)
        self.select_from_dropdown_by_visible_text(self.day, day)