from pycparser.c_ast import Return
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 🔹 Checkout Page Item Locators
    CHECK_OUT = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE = (By.XPATH, "//input[@id='continue']")
    CHECKOUT_PRICE = (By.XPATH, "//div[@class='summary_subtotal_label' and @data-test='subtotal-label']")
    CHECKOUT_PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
    PRICE_WITHOUT_TAX = (By.XPATH, "//div[@class='summary_subtotal_label']")

    def click_checkout_button(self):
        """Checkout and fill the details"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECK_OUT)).click()

    def fill_checkout_page(self, first_name, last_name, pincode):
        """Fill the form in checkout page"""
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(pincode)
        self.driver.find_element(*self.CONTINUE).click()

    def checkout_cart_price(self) -> str:
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.CHECKOUT_PRICE)
        price = self.driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text
        return price

    def checkout_products_sum(self) -> float:
        """Finds and returns the sum of all the prices of products in inventory page"""
        total_price = 0.00
        prices = self.driver.find_elements(*self.CHECKOUT_PRICES)
        for price in prices:
            total_price += float(price.text.replace('$', ''))  # Convert price to float
        return total_price  # Return only the sum

    def get_checkout_page_price_without_tax(self) -> float:
        price = self.driver.find_element(*self.PRICE_WITHOUT_TAX).text
        price = price.split("$")[-1]
        return float(price)

    def is_checkout_disabled(self):
        """Checks if checkout button is disabled"""
        checkout_buttons = self.driver.find_elements(By.ID, "checkout")
        return not bool(checkout_buttons)  # If no checkout button, means it's disabled

