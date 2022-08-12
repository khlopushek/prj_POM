from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import math


class ProductPage(BasePage):

    def add_to_basket(self):
        self.add_button= self.browser.find_element(*ProductPageLocators.ADD_BUTTON_CSS)
        self.add_button.click()

    def should_be_valid_message(self):
        self.message_actual = self.browser.find_element(*ProductPageLocators.MESSAGE_ACTUAL_CSS)
        self.msg_actual = self.message_actual.text
        self.message = self.browser.find_element(*ProductPageLocators.MESSAGE_CSS)
        self.msg = self.message.text       
        assert self.msg_actual == self.msg, "Actual and expected messages are different"

    def should_be_item_price(self):
        self.item_price_act = self.browser.find_element(*ProductPageLocators.PRICE_ACTUAL_CSS)
        self.price_act = self.item_price_act.text
        print(self.price_act)
        self.item_price_msg = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE_CSS)
        self.price_msg = self.item_price_msg.text
        print(self.price_msg)
        assert self.price_act == self.price_msg, "Actual price and price in the message are different"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def is_not_element_present(self):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
