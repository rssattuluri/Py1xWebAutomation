import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.positive
def test_vwologin_positive():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    # driver.implicitly_wait(20)

    username = driver.find_element(By.XPATH, "//input[@id='login-username']")
    username.send_keys(os.getenv("EMAIL"))

    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys(os.getenv("PASSWORD"))

    sign_in = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in.click()
    # time.sleep(20)


    #    WebDriverWait(driver,15).until(
    #  EC.url_contains("dashboard") - dashboard is taken from url-https://app.vwo.com/#/dashboard
    #       EC.text_to_be_present_in_element((By.XPATH, "//h1[@class='page-heading']"), "Dashboard")
    #    )

    # Fluent wait - condition+frequency = customize exception
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=15, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading")))
    assert "Dashboard" in element.text

    # PF = 1  EF = NO, t < 15 , WD - Should Exception ?
    # PF = 2  EF = NO, m < 10 , WD - Should Exception ?
    # ......
    # PF = 15  EF = NO, m = 15 , WD - Should Exception Yes

    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert heading_element.text == os.getenv("USERNAME")
    driver.quit()
