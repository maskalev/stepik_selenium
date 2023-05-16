import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 20

# @pytest.mark.parametrize(
#         'path', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
#         )
@pytest.mark.parametrize(
        'path', ["236898", "236899", "236905"]
        )
class Test_365():
    def test_365(self, browser: webdriver.Chrome, path: str) -> None:
        browser.get(f"https://stepik.org/lesson/{path}/step/1")
        answer = math.log(int(time.time()))
        WebDriverWait(browser, TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(answer))
        WebDriverWait(browser, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission"))
        )
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(TIMEOUT)
        browser.find_element(By.CLASS_NAME, "again-btn").click()
        print("\ntest end...")

        

if __name__ == "__name__":
    obj = Test_365()
    obj.test_365()
