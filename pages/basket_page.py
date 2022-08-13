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
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.message_actual = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        self.msg_actual = self.message_actual.text
        assert "Your basket is empty" in self.msg_actual, "Basket is not empty"

    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Product is presented, but should not be, basket is not empty"

       