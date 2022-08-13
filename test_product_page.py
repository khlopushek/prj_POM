import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.links import MainPageLinks
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators


#def test_guest_can_go_to_login_page(browser):
#    page = MainPage(browser, MainPageLinks.link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()

#def test_guest_should_see_login_link(browser):
#    page = MainPage(browser, MainPageLinks.link)
#    page.open()
#    page.should_be_login_link()


#def test_guest_can_add_product_to_basket(browser):
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_to_basket()
#    product_page.solve_quiz_and_get_code()
#    product_page.should_be_valid_message()
#    product_page.should_be_item_price()

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_to_basket()
#    assert product_page.is_not_element_present(*ProductPageLocators.MESSAGE_CSS), \
#      "Success message is presented, but should not be"


#def test_guest_cant_see_success_message(browser): 
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_CSS), \
#      "Success message is presented, but should not be"

#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_to_basket()
#    assert product_page.is_disappeared(*ProductPageLocators.MESSAGE_CSS), \
#      "Success message is presented, but should not be"    

#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_login_link()


#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_login_page()


#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = BasePage(browser, link)
#    page.open()
#    page.go_to_basket()
#    page_basket = BasketPage(browser, browser.current_url)
#    page_basket.should_be_empty_basket()
#    page_basket.should_be_no_products()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope = "function", autouse = True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.reg_page = BasePage(browser, link)
        self.reg_page.open()
        self.reg_page.go_to_login_page()
        self.register = LoginPage(browser, browser.current_url)
        email = str(str(time.time()) + "@fakemail.org")
        password = "eeelllkkkkkk"
        self.register.register_new_user(email, password)
        self.reg_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        page = MainPage(browser, MainPageLinks.link_promo) 
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.MESSAGE_CSS), \
          "Success message is presented, but should not be" 


    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, MainPageLinks.link_promo) 
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_valid_message()
        product_page.should_be_item_price()
