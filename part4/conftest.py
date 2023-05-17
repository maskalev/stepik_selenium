import sys
import time
from pathlib import Path
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__FILE_PATH__ = Path(__file__).parent.absolute()
sys.path.append(f"{__FILE_PATH__}")

from pages.login_page import LoginPage  # type: ignore
from pages.product_page import ProductPage  # type: ignore


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--language", action="store", default="en")


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[webdriver.Chrome, None, None]:
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def login(browser: webdriver.Chrome) -> None:
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time())
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()
