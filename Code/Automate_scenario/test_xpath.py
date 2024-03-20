from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_xpath():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"

    # make_app_btn = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    # make_app_btn_text = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    # make_app_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(),'Make App')]")
   #  make_app_btn_partial.click()
    # //a[starts-with(text(),'Make')]
    # End-with

    list_elements_p = driver.find_elements(By.XPATH , "//p[contains(text(),'A')]")
    for i in list_elements_p:
       if i.text == 'Copyright':
          i.click()
       print(i.text)

# Xpath OR and AND
# //p[contains(text(),'A') and contains(@class,'mute')] - single element
# //p[contains(text(),'A') or contains(@class,'mute')] - multiple elements

# id -> name -> classname -> cssslector -> xpath (Direct) -> xpath functions -> xpath axes


    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    # driver.get("https://www.idrive360.com/enterprise/login")

   # abs_xpath = driver.find_element(By.XPATH, "//*[@id="login-username"]")
   # abs_xpath.send_keys("admin")

   # rel_xpath = driver.find_element(By.XPATH, "//input[@type='email']")
   # rel_xpath.send_keys("admin")

    # rel_xpath1 = driver.find_element(By.XPATH, "//*[@id='password']")
    # rel_xpath1.send_keys("123")

    # time.sleep(2000)