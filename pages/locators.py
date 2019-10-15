from selenium.webdriver.common.by import By




class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """Локаторы страницы регистрации и атворизации"""

    # ---- Login Form Locators
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#login_form input[type=email]")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#login_form input[type=password]")
    LOGIN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login_form p>a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form [type=submit]")
    LOGIN_FORM = (By.ID, "login_form")

    # ---- Register Form Locators
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form [type=email]")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form [type=password]")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form [type=submit]")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    """Локаторы страницы продукта"""
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type=submit]")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div#content_inner h1")
    PRICE = (By.CSS_SELECTOR, "div#content_inner p.price_color")

    BASKET_FULL_PRICE = (By.CSS_SELECTOR, "#messages  div > p:nth-child(1) > strong")

    MESSAGE_BASKET = (By.CSS_SELECTOR, "#messages strong")
