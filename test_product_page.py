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


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, MainPageLinks.link_promo) 
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_valid_message()
    product_page.should_be_item_price()


#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
#    page = MainPage(browser, MainPageLinks.link_promo) 
#   page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_to_basket()
#    product_page.is_not_element_present()

#def test_guest_cant_see_success_message(): 
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    message = 
#    message.is_not_element_present()

#def test_message_disappeared_after_adding_product_to_basket():
#    page = MainPage(browser, MainPageLinks.link_promo) 
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_to_basket()
#    message = 
#    message.is_dissapeared()    

