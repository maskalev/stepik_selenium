import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 5

def test_button_add_to_basket(browser: webdriver.Chrome) -> None:
	WebDriverWait(browser, TIMEOUT).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
	)
	assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) == 1, "Button not found"
