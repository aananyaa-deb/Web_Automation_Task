import pytest
from selenium.webdriver.common.by import By
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage

def test_add_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Add first two items to cart
    inventory_page.add_first_two_items_to_cart()

    # Verify cart badge count (should be 2)
    assert inventory_page.get_cart_badge_count() == 2, "Cart badge count is incorrect!"

    # Go to cart and verify items are present
    inventory_page.click_cart_icon()
    assert cart_page.get_cart_item_count() == 2, "Cart does not contain the correct items!"

    # Edge Case: Remove all items and verify badge disappears
    cart_page.remove_all_items()
    assert inventory_page.get_cart_badge_count() == 0, "Cart badge should be empty after removing items!"
