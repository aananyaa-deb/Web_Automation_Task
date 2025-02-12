import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Create an explicit wait instance
    driver.wait = WebDriverWait(driver, 10)  # Attach wait object to driver

    yield driver  # Provide the driver instance to test functions

    driver.quit()  # Close the browser after test execution
