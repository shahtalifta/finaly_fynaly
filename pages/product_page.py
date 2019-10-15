from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_button_add_to_basket()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET)

    def should_be_name_inner(self):
        assert WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.NAME_PRODUCT))

    def should_be_price_product(self):
        assert WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.PRICE))

    def button_add_to_basket(self):
        button = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.BUTTON_ADD_BASKET))
        button.click()

    def get_product_name(self):
        name_product = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.NAME_PRODUCT))
        return name_product.text

    def get_product_price(self):
        price_product = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.PRICE))
        return price_product.text

    def get_full_basket_price(self):
        full_basket_price = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_FULL_PRICE))
        return full_basket_price.text

    def message_basket(self):
        message = WebDriverWait(self.browser, 10, NoSuchElementException).until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_BASKET))
        return message.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BASKET), \
            "Success message is presented, but should not be"

    def hidden_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BASKET)


    def comparison_price_end_name(self, name: str, price: str):
        ...
