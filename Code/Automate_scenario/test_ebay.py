import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    assert driver.current_url == "https://www.ebay.com/"

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    # CSS selector -> input[id='gh-ac']
    search_box.send_keys("16 gb laptop")

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    # input[id='gh-btn']
    search_btn.click()
    time.sleep(5)

    list_results = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for i in list_results:
        if i.text == "Dell":
            i.click()
        print(i.text)