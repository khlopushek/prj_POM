import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
import math
from selenium.webdriver.support.ui import WebDriverWait
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        self.reg_email.send_keys(email)
        self.reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        self.reg_password.send_keys(password)
        self.confirm_password = self.browser.find_element(*LoginPageLocators.REG_CONFIRM)
        self.confirm_password.send_keys(password)
        self.register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        self.register_button.click()
        