import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 🔹 Inventory Item Locators
    SAUCE_LABS_BACKPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    ALL_ITEMS = (By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory ']")
    CART_PRICE = (By.XPATH, "//")


    # 🔹 Methods for Interactions
    def add_backpack_to_cart(self):
        """Click on 'Add to Cart' for the backpack."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SAUCE_LABS_BACKPACK)
        ).click()

    def go_to_cart(self):
        """Click on the shopping cart icon."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def get_item_price(self) -> str:
        """Get the price of the item."""
        return self.driver.find_element(*self.ITEM_PRICE).text

    def add_all_items_to_cart(self):
        """Add all the items in inventory to the cart"""
        # true → Scrolls until the element is at the top of the viewport.
        # false → Scrolls until the element is at the bottom of the viewport.
        products = self.driver.find_elements(*self.ALL_ITEMS)
        for product in products :
            self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
            product.click()

    def add_bike_light_to_cart(self):
        """Add Bike Light to cart"""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    def remove_backpack_from_cart(self):
        """Removes backpack from cart"""
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def get_cart_item_count(self):
        """Returns the number of items in the cart"""
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0  # Returns 0 if cart is empty

    def logout_user(self):
        """Logs out the user"""
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

