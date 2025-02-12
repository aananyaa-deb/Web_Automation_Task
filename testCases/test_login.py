import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login_page import LoginPage  # Import the LoginPage class

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver)

    # Perform login
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Verify login success by checking the "Products" page header
    header_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
    assert header_text == "Products", "Login failed! 'Products' header not found."

def test_invalid_login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver)

    # Perform login with invalid credentials
    login_page.setUsername("wrong_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Verify error message
    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))).text
    assert "Epic sadface" in error_message, "Error message not displayed for invalid login!"

