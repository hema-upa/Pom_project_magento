import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.createaccountpage import CreateAccount



def test_create_account():
    # Initialize WebDriver using configuration
    driver = TestData.get_webdriver(TestData.BROWSER)

    driver.implicitly_wait(10)

    try:
        # Open the target URL
        driver.get(TestData.BASE_URL + "/customer/account/create/")
        driver.maximize_window()
        # Create an instance of CreateAccountPage
        create_account_page = CreateAccount(driver)

        # Define field locators and values
        field_locators_and_values = {
            "firstname": ((By.ID, "firstname"), "Hema"),
            "lastname": ((By.ID, "lastname"), "Upadhayay"),
            "email": ((By.ID, "email_address"), "hemaupadhayay92@gmail.com"),
            "password":((By.ID, "password"), "hema@123"),
            "confirm_password":((By.NAME, "password_confirmation"),"hema@123")
        }

        # Fill out the form
        create_account_page.create_new_customer_account(field_locators_and_values, (By.XPATH, f'//*[@id="form-validate"]/div/div[1]/button'))

        # Optionally, check for a confirmation message or successful submission
        # success_message = driver.find_element(By.ID, "success_message_id").text
        # assert "Account created successfully" in success_message

    except Exception as e:
        print(f"Test Failed: {e}")

    finally:
        # Clean up and close the browser
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_create_account()
