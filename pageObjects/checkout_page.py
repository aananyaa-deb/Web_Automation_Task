from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Increased timeout to 15 seconds

        self.checkout_header = (By.CLASS_NAME, "title")  # Ensuring checkout page is loaded
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def enter_checkout_info(self, first_name, last_name, postal_code):
        # Wait for checkout page to load
        self.wait.until(EC.text_to_be_present_in_element(self.checkout_header, "Checkout: Your Information"))

        # Enter details
        self.wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.last_name_field)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(self.postal_code_field)).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def verify_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text
