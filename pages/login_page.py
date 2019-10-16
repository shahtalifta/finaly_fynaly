from .base_page import BasePage
import time
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        assert "/login" in self.browser.current_url, "login is not current url"

    # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not available"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form not available"

    def register_new_user(self, email: str, password: str):
        input_email = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTRATION_EMAIL_INPUT))
        input_email.send_keys(email)
        input_password = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTRATION_PASSWORD_INPUT))
        input_password.send_keys(password)
        input_repeat_password = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTRATION_PASSWORD_REPEAT))
        input_repeat_password.send_keys(password)
        button = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTRATION_BUTTON))
        button.click()
        # return email, password
