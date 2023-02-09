from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def text_basket_is_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert basket_text=="""Your basket is empty. Continue shopping""", f"need (Your basket is empty. Continue shopping), but got ({basket_text})"

    def busket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Item in basket is presented, but should not be"
