from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest


def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    name_product = page.get_product_name()
    price_product = page.get_product_price()

    page.button_add_to_basket()
    page.solve_quiz_and_get_code()
    assert price_product == page.get_full_basket_price()
    assert name_product == page.get_product_name()
    assert name_product == page.message_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.your_basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Qweqwe_123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_to_basket()
        page.button_add_to_basket()
