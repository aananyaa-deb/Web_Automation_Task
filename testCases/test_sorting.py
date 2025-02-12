from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage


def test_sorting_products(setup):
    driver = setup
    login_page = LoginPage(driver)  # Fix: Use the correct class name 'LoginPage'
    inventory_page = InventoryPage(driver)

    # Step 1: Login
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Sorting by Price (Low to High)
    inventory_page.sort_products("Price (low to high)")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices), "Sorting by 'Price (low to high)' failed!"

    # Sorting by Price (High to Low)
    inventory_page.sort_products("Price (high to low)")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Sorting by 'Price (high to low)' failed!"

    # Sorting by Name (A to Z)
    inventory_page.sort_products("Name (A to Z)")
    names = inventory_page.get_product_names()
    assert names == sorted(names), "Sorting by 'Name (A to Z)' failed!"

    # Sorting by Name (Z to A)
    inventory_page.sort_products("Name (Z to A)")
    names = inventory_page.get_product_names()
    assert names == sorted(names, reverse=True), "Sorting by 'Name (Z to A)' failed!"
