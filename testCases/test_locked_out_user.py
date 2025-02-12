import pytest
from selenium.webdriver.common.by import By
from pageObjects.login_page import LoginPage


def test_locked_out_user(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Step 1: Go to the login page (already handled in setup)

    # Step 2: Enter the locked-out user's credentials
    login_page.setUsername("locked_out_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Step 3: Verify the error message
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

    # Assert the error message, updating the expected text to match the actual message
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out.", "Error message is incorrect!"
