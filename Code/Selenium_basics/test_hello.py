from selenium import webdriver
import time
# we have imported a class name webdriver
def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    #Give some extra arguments or extensions or anything
    extension_path = "This PC/Downloads/adblokcer.crdownload"
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome() # from webdriver class, we have imported chrome instance
    # Create a session with POST request (API post request)
    # fresh chrome browser will open, session ID is created
    driver.get("https://google.com")
    # get - load a webpage in the current browser session
    # GET request
    driver.maximize_window()
    print(driver.title)
    time.sleep(2000)


