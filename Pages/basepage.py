import time
from typing import Tuple
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from utils.logger import Logger
# this class is the parent class of all class


class BasePage:
    def __init__(self, driver: WebDriver)->None:
        self.driver = driver
        self.logger = Logger.setup_logger(self.__class__.__name__, 'base_page.log')

    def do_click(self, locator: Tuple[str, str]):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        self.logger.info("Performing an action on the base page.")
        
    def send_input(self, locator: Tuple[str, str], inputValue):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(inputValue)

    def get_text(self, locator):

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text
    
    def get_url(self, url):
        self.driver.implicitly_wait(10)
        self.driver.get(url)
    
    def go_back(self):
        self.driver.back()
    
    def go_forward(self):
        self.driver.forward()
    
    def refresh_page(self):
        self.driver.refresh()

    # Dynamic elements

    def is_element_visible(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
        
    def select_dropdown_by_value(self, locator, value):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(locator)))
        select.select_by_value(value)


    def scroll_to_element(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    #alerts

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present()).accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present()).dismiss()

    #javascript execution in terms of hidden elements

    def execute_javascript(self, script):
        return self.driver.execute_script(script)