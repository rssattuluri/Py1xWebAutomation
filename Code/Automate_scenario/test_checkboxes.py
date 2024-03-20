import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkbox_testing():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.maximize_window()

    # Click for JS Prompt
 #   checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # Check the Checkbox which is not selected
#    for c in checkboxes:
#        if not c.is_selected():
#            c.click()

# if want to click only one element
    checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'])[1]")
    checkbox_1.click()
    time.sleep(10)

    if not checkbox_1.is_selected():
        checkbox_1.click()
