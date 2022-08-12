from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser_url = self.browser.current_url
        assert "login" in self.browser_url, "Login link is not presented"

    def should_be_login_form(self):
        self.login_form = self.browser.find_element(*LoginPageLocators.LOGIN_CSS)
        assert EC.presence_of_element_located(self.login_form), "Login form is not presented"

    def should_be_register_form(self):
        self.register_form = self.browser.find_element(*LoginPageLocators.REGISTER_CSS)
        assert EC.presence_of_element_located(self.register_form), "Register form is not presented"