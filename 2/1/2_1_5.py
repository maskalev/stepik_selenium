import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    time.sleep(10)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
