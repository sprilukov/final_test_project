from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_bucket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_BUY)
        button_add_product.click()
    
    def check_product_name_add(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_product_name = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BUCKET).text
        assert product_name==add_product_name, f"add {product_name}, but added {add_product_name}"

    def check_product_price_add(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        bucket_price = self.browser.find_element(*ProductPageLocators.BUCKET_PRICE).text
        assert product_price==bucket_price, f"add {product_price}, but added {bucket_price}"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def is_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "is_disappeared_message"