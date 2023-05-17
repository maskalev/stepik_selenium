import math
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    __DIR_PATH__ = Path(__file__).parent.absolute()

    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("qwerty")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("asd")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("a@a")
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(f"{__DIR_PATH__}/file.txt")
    browser.find_element(By.CSS_SELECTOR, "button").click()

except:
    ...

finally:
    time.sleep(5)
    browser.quit()
