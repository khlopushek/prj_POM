from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_CSS = (By.CSS_SELECTOR, "#register_form")
    LOGIN_CSS = (By.CSS_SELECTOR, "#login_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    
    MESSAGE_ACTUAL_CSS = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    MESSAGE_CSS = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    
    PRICE_ACTUAL_CSS = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRICE_MESSAGE_CSS = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")

    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "header.header .basket-mini .btn-default")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT = (By.CSS_SELECTOR, "#content_inner > .basket-title > .row > h2.col-sm-6")
        