import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.get(f"https://stepik.org/lesson/236895/step/1")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "ember33"))
    )
    browser.find_element(By.ID, "ember33").click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    browser.find_element(By.ID, "id_login_email").send_keys("ya.maskalev@yandex.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("tdat$E57R2%rfMVWzVzU")
    browser.find_element(By.CSS_SELECTOR, "#login_form button").click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "navbar__profile-img"))
    )
    print("\nsuccessful login...")
    yield browser
    print("\nquit browser...")
    browser.quit()
