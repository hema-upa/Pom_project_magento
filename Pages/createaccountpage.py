from Pages.basepage import BasePage # just tells the availabilty of the base page doesn't give permission to access page.
import time
from typing import Tuple
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium import webdriver

class CreateAccount(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        #calling base class's constructor 
        super().__init__(driver)

    def go_to_create_account(self, locator):
        self.do_click(locator)

    def create_new_customer_account(self, field_values: dict[str,Tuple[str, str]], submit_loc: Tuple[str,str]):
        
        # Will iterate on every field in the dictionary and type associated value to it.
        for field in field_values:
            # print(field_values[field])
            self.send_input(*field_values[field])  # will take tupel value one by one 
        
        time.sleep(5)
        self.do_click(submit_loc)
    
        time.sleep(10)