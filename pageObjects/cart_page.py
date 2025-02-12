from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.remove_buttons = (By.CLASS_NAME, "cart_button")

        self.remove_button_locator = (By.CLASS_NAME, "cart_button")  # Update with the correct locator

    def get_cart_item_count(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        return len(items)

    def remove_all_items(self):
        remove_buttons = self.wait.until(EC.presence_of_all_elements_located(self.remove_buttons))
        for button in remove_buttons:
            button.click()

        # Method to get the number of items in the cart

    #def get_cart_item_count(self):
        #items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))  # Adjust selector
        #return len(items)

        # Method to remove an item from the cart

    def remove_item_from_cart(self, index):
        remove_buttons = self.wait.until(EC.presence_of_all_elements_located(self.remove_button_locator))
        remove_buttons[index].click()  # Click the remove button for the item at the given index
