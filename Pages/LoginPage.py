from Pages.basepage import BasePage # just tells the availabilty of the base page doesn't give permission to access page.
import time
from typing import Tuple
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium import webdriver

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        #calling base class's constructor
        super().__init__(driver)

    def sign_in(self, list_locator: list[Tuple[str, str]], submit_locator: Tuple[str, str] ):  
        for locator in list_locator:
            self.send_input(*locator)
        
        self.do_click(submit_locator)
        
        time.sleep(10)