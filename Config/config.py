# config/config.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class TestData:
    # Base URL for the application under test
    BASE_URL = "https://magento.softwaretestingboard.com/"
    
    # Browser settings
    BROWSER = "chrome"

    # WebDriver options
    CHROME_OPTIONS = [
        "--disable-gpu",
        #"--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]

    FIREFOX_OPTIONS = [
        "--headless"
    ]

    def get_webdriver(browser):
        if browser == 'chrome':
            options = Options()
            for option in TestData.CHROME_OPTIONS:
                options.add_argument(option)
            service = Service(ChromeDriverManager().install())
            driver_ch = webdriver.Chrome(service=service)
            return driver_ch
            
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            for option in TestData.FIREFOX_OPTIONS:
                options.add_argument(option)
            return webdriver.Firefox(GeckoDriverManager().install(), options=options)
        
        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            return webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {browser}")

