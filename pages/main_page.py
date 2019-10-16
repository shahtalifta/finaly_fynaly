from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_page(self):
        go_basket = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(MainPageLocators.VIEW_BASKET))
        go_basket.click()
