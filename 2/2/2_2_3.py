import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = num2.text
    result = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
