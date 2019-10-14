from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Локаторы страницы регистрации и атворизации"""
    # ---- Login Form Locators
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#login_form input[type=email]")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#login_form input[type=password]")
    LOGIN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login_form p>a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form [type=submit]")
    LOGIN_FORM = (By.ID, "#login_form")

    # ---- Register Form Locators
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form [type=email]")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form [type=password]")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form [type=submit]")
    REGISTRATION_FORM = (By.ID, "#register_form")
