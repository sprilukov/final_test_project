from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER = (By.ID, "id_registration-email")
    PASSWORD_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM_REGISTER = (By.ID, "id_registration-password2")
    CONFIRM_REGISTRATION = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_BUY = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADD_PRODUCT_TO_BUCKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main > .price_color")
    BUCKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")