import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
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

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product()    
    time.sleep(2)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, link)
    page.open()    
    time.sleep(2)
    page.should_not_be_success_message()
 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()    
    page.add_product()   
    time.sleep(2)
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_basket_message()