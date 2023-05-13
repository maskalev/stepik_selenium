import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    value = browser.find_element(By.ID, "input_value").text
    result = calc(int(value))
    browser.find_element(By.ID, "answer").send_keys(str(result))
    browser.find_element(By.ID, "solve").click()


except Exception as e:
    print(e)

finally:
    time.sleep(5)
    browser.quit()
