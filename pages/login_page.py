from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'It isnt login link!'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_REGISTER)
        password_confirm_input.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION)
        button_registration.click()
