import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
import time

initial_url = ProductPageLocators.product_url
urls = [f"{initial_url}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product()    
    time.sleep(2)
