import pytest
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage
from pageObjects.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_checkout_process(setup):
    driver = setup
    wait = WebDriverWait(driver, 15)

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Step 1: Login
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLogin()

    # Step 2: Add product to cart
    inventory_page.add_first_two_items_to_cart()

    # Step 3: Proceed to cart and checkout
    inventory_page.click_cart_icon()
    cart_page.get_cart_item_count()  # Ensure items are present

    # **Fix:** Explicit wait for checkout button to appear and click it
    checkout_button = (By.ID, "checkout")
    wait.until(EC.element_to_be_clickable(checkout_button)).click()

    # Step 4: Enter checkout information
    checkout_page.enter_checkout_info("John", "Doe", "12345")
    checkout_page.click_continue()

    # Step 5: Complete the order
    checkout_page.click_finish()

    # Step 6: Verify success message
    success_text = checkout_page.verify_success_message()
    assert success_text == "Thank you for your order!", "Order completion failed!"
