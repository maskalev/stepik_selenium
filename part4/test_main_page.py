import sys
from pathlib import Path

import pytest
from selenium import webdriver

__FILE_PATH__ = Path(__file__).parent.absolute()
sys.path.append(f"{__FILE_PATH__}")

from pages.basket_page import BasketPage  # type: ignore
from pages.login_page import LoginPage  # type: ignore
from pages.main_page import MainPage  # type: ignore


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser: webdriver.Chrome) -> None:
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser: webdriver.Chrome) -> None:
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(
    browser: webdriver.Chrome,
) -> None:
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_empty_basket()
    basket_page.is_empty_basket_message()
