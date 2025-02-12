from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit wait with a timeout of 10 seconds
        self.textbox_username_id = "user-name"
        self.textbox_password_id = "password"
        self.button_login_id = "login-button"
        self.menu_button_id = "react-burger-menu-btn"
        self.logout_id = "logout_sidebar_link"

        self.logout_button = (By.ID, "logout_sidebar_link")  # assuming this is the logout button
        self.login_page_locator = (By.ID, "login-button")  # We assume the login button appears on the login page

    def setUsername(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.button_login_id)))
        login_button.click()

    def clickMenu(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.menu_button_id)))
        menu_button.click()

    def clickLogout(self):
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.logout_id)))
        logout_button.click()

    def clickLogout(self):
        self.driver.find_element(*self.logout_button).click()

    def is_login_page_displayed(self):
        # Check if the login button is present, indicating the user is on the login page
        return self.driver.find_element(*self.login_page_locator).is_displayed()

