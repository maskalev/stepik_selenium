import sys
from pathlib import Path

import pytest
from selenium import webdriver

__FILE_PATH__ = Path(__file__).parent.absolute()
sys.path.append(f"{__FILE_PATH__}")

from pages.basket_page import BasketPage  # type: ignore
from pages.login_page import LoginPage  # type: ignore
from pages.product_page import ProductPage  # type: ignore


class TestGuestGoToLoginPageFromProductPage:
    def test_guest_should_see_login_link_on_product_page(
        self,
        browser: webdriver.Chrome,
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(
        self,
        browser: webdriver.Chrome,
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser: webdriver.Chrome) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_into_basket()
        page.check_item_name_in_basket()
        page.check_price_in_basket()

    @pytest.mark.xfail(reason="special bad test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(
        self,
        browser: webdriver.Chrome,
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_into_basket()
        page.sucess_message_is_not_present()

    def test_guest_cant_see_success_message(self, browser: webdriver.Chrome) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.sucess_message_is_not_present()

    @pytest.mark.xfail(reason="special bad test")
    def test_message_disappeared_after_adding_product_to_basket(
        self,
        browser: webdriver.Chrome,
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_into_basket()
        page.sucess_message_is_disappeared()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(
        self,
        browser: webdriver.Chrome,
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_empty_basket()
        basket_page.is_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(
        self, browser: webdriver.Chrome, login: None
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.sucess_message_is_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(
        self, browser: webdriver.Chrome, login: None
    ) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_into_basket()
        page.check_item_name_in_basket()
        page.check_price_in_basket()
