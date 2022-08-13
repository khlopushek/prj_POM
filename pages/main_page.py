import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):

#    def go_to_login_page(self):
#        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        link.click()
#        return LoginPage(browser=self.browser, url=self.browser.current_url) 
#        alert = self.browser.switch_to.alert
#        alert.accept()

#    def should_be_login_link(self):
#        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)