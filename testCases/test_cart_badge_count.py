import pytest
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage
from selenium.webdriver.common.by import By


def test_cart_badge_count(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Login to the app
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Step 2: Add multiple products to the cart
    inventory_page.add_first_two_items_to_cart()  # Assuming you want to add the first two items

    # Step 3: Verify the cart badge shows the correct item count (should be 2)
    cart_badge_count = inventory_page.get_cart_badge_count()
    assert cart_badge_count == 2, f"Expected cart badge count to be 2, but got {cart_badge_count}"

    # Step 4: Go to the cart and verify items are present
    inventory_page.click_cart_icon()
    cart_item_count = cart_page.get_cart_item_count()
    assert cart_item_count == 2, f"Expected 2 items in the cart, but got {cart_item_count}"

    # Step 5: Remove one item from the cart
    cart_page.remove_item_from_cart(0)  # Assuming the method removes the item at index 0

    # Step 6: Verify the cart badge count updates (should be 1)
    updated_cart_badge_count = inventory_page.get_cart_badge_count()
    assert updated_cart_badge_count == 1, f"Expected cart badge count to be 1, but got {updated_cart_badge_count}"

    # Step 7: Verify that the cart now contains only 1 item
    updated_cart_item_count = cart_page.get_cart_item_count()
    assert updated_cart_item_count == 1, f"Expected 1 item in the cart, but got {updated_cart_item_count}"

    cart_page.remove_item_from_cart(0)
