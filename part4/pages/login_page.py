import time

from pages.base_page import BasePage  # type: ignore
from pages.locators import LoginPageLocators  # type: ignore


class LoginPage(BasePage):  # type: ignore
    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert (
            "/login/" in self.browser.current_url
        ), "Theren't login url in current url"

    def should_be_login_form(self) -> None:
        assert self.is_form_present(
            LoginPageLocators.LOGIN_FORM_FULL
        ), "Login form is not presented or is not full"

    def should_be_register_form(self) -> None:
        assert self.is_form_present(
            LoginPageLocators.REGISTRATION_FORM_FULL
        ), "Register form is not presented or is not full"

    def register_new_user(self, email: str, password: str) -> None:
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(
            email
        )
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(
            password
        )
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD
        ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
