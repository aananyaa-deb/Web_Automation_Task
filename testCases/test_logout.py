import pytest
from selenium.webdriver.common.by import By
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage

def test_logout_functionality(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Step 1: Login with valid credentials
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Step 2: Click the hamburger menu (☰) in the top-left corner
    inventory_page.clickMenu()  # Assuming this method opens the menu

    # Step 3: Click Logout
    inventory_page.clickLogout()  # This method clicks the logout button in the menu

    # Step 4: Verify that the user is redirected to the login page
    assert login_page.is_login_page_displayed(), "User is not redirected to the login page after logout!"
