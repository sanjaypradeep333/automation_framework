# tests/test_login.py
import time
import pytest
from utils.excel_utils import get_test_data
from pages.checkout_page import Checkout_Page
from pages.LoginPage import LoginPage
from pages.inventory_page import InventoryPage
from utils.xml_utils import get_test_data_from_xml

file_path = r"C:\Users\sanja\automation_framework\data\testdata.xlsx"
test_data = get_test_data(file_path, "LoginData")

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_with_excel_data(setup, logger, username, password, expected):
    """Test login functionality with data from Excel."""
    logger.info(f"Starting login test with Excel data: username={username}")
    login_page = LoginPage(setup)

    logger.info("Entering username and password")
    login_page.enter_username(username)
    login_page.enter_password(password)
    logger.info("Clicking login button")
    login_page.click_login()

    if expected == "success":
        assert "inventory.html" in setup.current_url, "Login failed!"
        logger.info("Login test passed - reached inventory page")
    else:
        error_msg = login_page.get_error_message()
        assert "Epic sadface" in error_msg, "Error message not displayed!"
        logger.info("Login test passed - error message displayed")

file_path = r"C:\Users\sanja\automation_framework\data\testdata.xml"
test_data = get_test_data_from_xml(file_path)

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_with_xml_data(setup, logger, username, password, expected):
    """Test login functionality with XML test data."""
    logger.info(f"Starting login test with XML data: username={username}")
    login_page = LoginPage(setup)

    logger.info("Entering username and password")
    login_page.enter_username(username)
    login_page.enter_password(password)
    logger.info("Clicking login button")
    login_page.click_login()

    if expected == "success":
        assert "inventory.html" in setup.current_url, "Login failed!"
        logger.info("Login test passed - reached inventory page")
    else:
        error_msg = login_page.get_error_message()
        assert "Epic sadface" in error_msg, "Error message not displayed!"
        logger.info("Login test passed - error message displayed")

def test_valid_login(setup, logger):
    """Test successful login with valid credentials."""
    logger.info("Starting valid login test")
    login_page = LoginPage(setup)

    logger.info("Entering valid credentials")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    logger.info("Clicking login button")
    login_page.click_login()

    assert "inventory.html" in setup.current_url, "Login failed!"
    logger.info("Valid login test passed")

def test_invalid_login(setup, logger):
    """Test login with invalid credentials."""
    logger.info("Starting invalid login test")
    login_page = LoginPage(setup)

    logger.info("Entering invalid credentials")
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_pass")
    logger.info("Clicking login button")
    login_page.click_login()

    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg, "Error message not displayed!"
    logger.info("Invalid login test passed - error message displayed")

def test_total_price_in_cart(setup, logger):
    """Test to verify total price of items in cart."""
    logger.info("Starting total price in cart test")
    login_page = LoginPage(setup)
    inventory_page = InventoryPage(setup)

    logger.info("Logging in")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    logger.info("Adding backpack to cart")
    inventory_page.add_backpack_to_cart()

    logger.info("Going to cart")
    inventory_page.go_to_cart()

    assert inventory_page.get_item_price() == "$29.99", "Price mismatch!"
    logger.info("Total price in cart test passed")

def test_validate_total_cart_amount(setup, logger):
    """Test to verify the inventory prices and total cart amount."""
    logger.info("Starting validate total cart amount test")
    login_page = LoginPage(setup)
    inventory_page = InventoryPage(setup)
    checkout_page = Checkout_Page(setup)

    logger.info("Logging in")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    logger.info("Adding all items to cart")
    cart_total = inventory_page.add_all_items_to_cart()

    logger.info("Going to cart and starting checkout")
    inventory_page.go_to_cart()
    checkout_page.click_checkout_button()
    logger.info("Filling checkout details")
    checkout_page.fill_checkout_page("Sanjay", "Pradeep", "516004")

    checkout_price = checkout_page.get_checkout_page_price_without_tax()
    calculated_price = checkout_page.checkout_products_sum()

    assert checkout_price == calculated_price, f"Price Mismatch! Checkout: {checkout_price}, Calculated: {calculated_price}"
    logger.info("Validate total cart amount test passed")
    print("✅ Validation successful. Checkout products price matches inventory sum.")

def test_remove_item_from_cart(setup, logger):
    """Test to verify cart price updates when an item is removed."""
    logger.info("Starting remove item from cart test")
    login_page = LoginPage(setup)
    inventory_page = InventoryPage(setup)

    logger.info("Logging in")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    logger.info("Adding items to cart")
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    logger.info("Going to cart and removing backpack")
    inventory_page.go_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.get_cart_item_count() == 1, "Cart count mismatch after removal!"
    logger.info("Remove item from cart test passed")
    print("✅ Item removed successfully, cart updated.")

def test_checkout_empty_cart(setup, logger):
    """Test to verify checkout button is disabled when cart is empty."""
    logger.info("Starting checkout empty cart test")
    login_page = LoginPage(setup)
    inventory_page = InventoryPage(setup)
    checkout_page = Checkout_Page(setup)

    logger.info("Logging in")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    logger.info("Going to cart with no items")
    inventory_page.go_to_cart()

    is_checkout_disabled = checkout_page.is_checkout_disabled()
    assert is_checkout_disabled, "Checkout allowed with an empty cart!"
    logger.info("Checkout empty cart test passed")
    print("✅ Checkout correctly disabled for empty cart.")

def test_logout_functionality(setup, logger):
    """Test to verify user can log out successfully."""
    logger.info("Starting logout functionality test")
    login_page = LoginPage(setup)
    inventory_page = InventoryPage(setup)

    logger.info("Logging in")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    logger.info("Logging out")
    inventory_page.logout_user()

    assert "saucedemo.com" in setup.current_url, "Logout failed!"
    logger.info("Logout functionality test passed")
    print("✅ Logout successful, user redirected to login page.")