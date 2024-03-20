import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_make_app():
    driver1 = webdriver.Chrome()
    driver1.get("https://katalon-demo-cura.herokuapp.com/")

    # click on Make appointment button
    # make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    # make_appointment_button.click()

    # map_bt = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment/ment/Make")
    # map_bt.click()

    # map_bt1 = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # map_bt1.click()

    # map_btn = driver.find_elements(By.CLASS_NAME, "btn btn-dark btn-lg")
    # map_btn[1].click()

    # map_btn1 = driver.find_elements(By.TAG_NAME, "a")
    # map_btn1[5].click()

    map_t = driver1.find_element(By.XPATH, '//a[contains(text(), "Make Appointment")]')
    map_t.click()

    print(driver1.current_url)
    assert driver1.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"

    username = driver1.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    password = driver1.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    login = driver1.find_element(By.ID, "btn-login")
    login.click()
    assert driver1.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"

    time.sleep(2000)
    driver1.quit()
