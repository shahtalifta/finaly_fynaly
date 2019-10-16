from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert "/basket" in self.browser.current_url

    def should_be_status_basket(self):
        assert WebDriverWait(self.browser, 5, NoSuchElementException).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_STATUS))


