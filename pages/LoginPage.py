from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators using relative XPath with axes
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error-message-container')]//h3")
    sauce_labs_backpack = (By.XPATH, "//div[text()='Sauce Labs Backpack' and @class='inventory_item_name ']/following::div[@class='pricebar'][1]/button[@id='add-to-cart-sauce-labs-backpack']")


    def enter_username(self, username: str):
        """Enter username in the login field."""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        """Enter password in the login field."""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self) -> str:
        """Retrieve the error message text if login fails."""
        return self.driver.find_element(*self.ERROR_MESSAGE).text
