import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.LoginPage import LoginPage
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time 

def test_login_valid_username_password():
    driver = TestData.get_webdriver(TestData.BROWSER)

    try:
        driver.get(TestData.BASE_URL + f'/customer/account/login')
        driver.maximize_window()
        time.sleep(5)
        login = LoginPage(driver)

        list_loc = [((By.ID, "email"), "hemaupadhayay92@gmail.com"), ((By.ID, "pass"), "hema@123")]
        button = (By.XPATH, f'//*[@id="send2"]')
        
        login.sign_in(list_loc, button)
    except Exception as e:
        print({e})

    finally:
        # Clean up and close the browser
        driver.quit()

    # Run the test

if __name__ == "__main__":
    test_login_valid_username_password()