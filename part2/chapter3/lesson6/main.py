import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    browser.find_element(By.CSS_SELECTOR, "button").click()
    print("start")
    print(browser.window_handles)
    print("end")
    browser.switch_to.window(browser.window_handles[1])
    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(int(value))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "button").click()


except Exception as e:
    print(e)

finally:
    browser.quit()
