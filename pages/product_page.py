from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

class ProductPage(BasePage):
    def add_product(self):
        try:
            self.browser.implicitly_wait(5)
            button = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
            button.click()
        except NoSuchElementException:
            print("Basket element not found")

        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert appeared")

    def naming_equality(self):
        assert self.item_name == self.item_bname, 'Naming is the same'

    def check_price_equality(self):
        assert self.item_price == self.total_price, 'Price is the same'