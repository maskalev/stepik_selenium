import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    result = calc(int(value))

    form = browser.find_element(By.CLASS_NAME, "form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", form)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

except:
    ...

finally:
    time.sleep(10)
    browser.quit()
