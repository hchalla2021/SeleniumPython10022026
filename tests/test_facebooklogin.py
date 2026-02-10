import pytest
import time
from pages.base_page import BasePage
from pages.facebookSign import FacebookSignPage
from selenium import webdriver
from utils.excelUtil import read_excel

test_data = read_excel("D:\\Trainings\\Selenium Python\\SeleniumPython_POM_Shama\\data\\data.xlsx", None)

@pytest.mark.parametrize("data_set", test_data)
def test_facebook_login(browser, config, data_set):
    browser.get(config['URL'])
    browser.maximize_window()
    time.sleep(5)
    fblogin = FacebookSignPage(browser)
    fblogin.login_facebook(data_set['Name'], data_set['mobile'], data_set['Password'])
    # Select day (default to 20 if 'day' column doesn't exist in Excel)
    day_value = data_set.get('day', '20')
    fblogin.select_day(str(day_value))

