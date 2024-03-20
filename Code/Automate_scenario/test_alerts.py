from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_alerts_testing():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    # Click for JS Prompt
    button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Ramya")
    alert.accept()
    # alert.dismiss() - to cancel the alert

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)

'''   
# Click for JS Alert
    button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)
'''
