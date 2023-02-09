from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_CONTENT), \
           "basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_disappeared(*BasePageLocators.BASKET_MESSAGE), \
           "non label basket empty"