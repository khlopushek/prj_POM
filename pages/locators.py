from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_CSS = (By.CSS_SELECTOR, "#register_form")
    LOGIN_CSS = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    
    MESSAGE_ACTUAL_CSS = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    MESSAGE_CSS = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    
    PRICE_ACTUAL_CSS = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRICE_MESSAGE_CSS = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")



        