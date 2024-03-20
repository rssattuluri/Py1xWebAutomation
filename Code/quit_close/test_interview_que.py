from selenium import webdriver

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.title) # Google
    # driver.close()   # close() will close the current window(tab), it will not close other tabs, Session != Null
    # driver.quit()   # quit() close all tabs(windows), session == None
    # Navigation commands
    driver.back() # takes us back to the previous page as per the browsing history
    driver.get("https://www.bing.com")
    print(driver.title) # Bing

    driver.forward() # takes us to the next page as per the browsing history
    print(driver.title) # Bing

    driver.back()
    print(driver.title)
    driver.refresh() # Google