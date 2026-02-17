from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import os
# This is local change 2026
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def __init__(self, driver):
        self.driver = driver

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)    

    def find_element(self, locator):
      return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def select_from_dropdown_by_visible_text(self, locator, text):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def takescreenshot(self, file_path):
       os.makedirs(os.path.dirname(file_path), exist_ok=True)
       self.driver.save_screenshot(file_path)
