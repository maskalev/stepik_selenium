import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.CSS_SELECTOR, "button").click()
    browser.switch_to.alert.accept()
    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(int(value))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(result))
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button").click()


except:
    ...

finally:
    time.sleep(5)
    browser.quit()
