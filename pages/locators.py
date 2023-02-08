from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    #product_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear/'
    #product_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019/'
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_name = (By.CSS_SELECTOR, '.row h1')
    item_bname = (By.CSS_SELECTOR, '.alertinner>strong')
    item_price = (By.CSS_SELECTOR, 'p.price_color')
    total_price = (By.CLASS_NAME, '.alertinner p strong')
