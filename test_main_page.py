import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.your_basket_is_empty()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/the-shellcoders-handbook_209/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
