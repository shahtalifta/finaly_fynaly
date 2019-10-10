from .pages.main_page import MainPage


# class TestMainPage(MainPage):
#     #     def test_running_auto_tests_for_different_interface_languages(self, browser):
#     #         browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     #         button_basket = WebDriverWait(browser, 3).until(
#     #             EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_to_basket_form > button[type=\'submit\']")))
#     #         assert button_basket
#     #
#     #         time.sleep(3)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()