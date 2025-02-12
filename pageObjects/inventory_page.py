from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # <-- Add this import
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")  # Cart badge locator
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")  # Dropdown for sorting products
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")  # Locator for product prices
        self.product_names = (By.CLASS_NAME, "inventory_item_name")

        self.menu_button = (By.ID, "react-burger-menu-btn")  # Locator for the hamburger menu button
        self.logout_button = (By.ID, "logout_sidebar_link")  # Locator for the logout button




    def add_first_two_items_to_cart(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.add_to_cart_buttons))
        for button in buttons[:2]:  # Click only the first two items
            button.click()

    def click_cart_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    # Fix: Correct the indentation of this method
    def sort_products(self, sort_option):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        dropdown.click()
        # Selecting the desired sorting option
        dropdown.find_element(By.XPATH, f"//option[text()='{sort_option}']").click()

    # Get Product Prices (For Sorting Validation)
    def get_product_prices(self):
        return [float(item.text.replace("$", "")) for item in
                self.wait.until(EC.presence_of_all_elements_located(self.product_prices))]

        # Get Product Names (For Sorting Validation)
    def get_product_names(self):
        return [item.text for item in self.wait.until(EC.presence_of_all_elements_located(self.product_names))]

    def get_cart_badge_count(self):
        try:
            badge = self.wait.until(EC.presence_of_element_located(self.cart_badge))
            return int(badge.text)  # Return the badge count as integer
        except:
            return 0  # If badge is not visible, return 0



    def clickMenu(self):
        self.driver.find_element(*self.menu_button).click()

    def clickLogout(self):
        # Ensure that the button is visible and clickable
        logout_button = self.driver.find_element(*self.logout_button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(logout_button))
        logout_button.click()