import os
import pytest

from pages.checkout_page import CheckoutPage
from utils.create_driver import create_driver
from config.config_reader import valid_creds, base_url

from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default=None)
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--headless", action="store", default=False)

@pytest.fixture(scope="session", autouse=True)
def set_env_vars(request):
    if request.config.getoption("--base_url"):
        os.environ["BASE_URL"] = request.config.getoption("--base_url")
    if request.config.getoption("--browser_name"):
        os.environ["BROWSER_NAME"] = request.config.getoption("--browser_name")
    if request.config.getoption("--headless"):
        os.environ["HEADLESS"] = request.config.getoption("--headless")

@pytest.fixture()
def driver():
    browser = os.getenv("BROWSER_NAME", "chrome").lower()
    headless = os.getenv("HEADLESS", False)
    driver = create_driver(browser, headless)
    driver.maximize_window()
    driver.get(base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    # Returns Login Page object
    return LoginPage(driver)

@pytest.fixture()
def logged_in_driver(driver, login_page):
    # Performs login for tests that need user to be logged in
    login_page.login(valid_creds())
    return driver

@pytest.fixture()
def products_page(logged_in_driver):
    # Returns Products Page object
    return ProductsPage(logged_in_driver)

@pytest.fixture()
def product_details_page(logged_in_driver):
    # Returns Product Details Page object
    return ProductDetailsPage(logged_in_driver)

@pytest.fixture()
def cart_page(logged_in_driver):
    # Returns cart page object
    return CartPage(logged_in_driver)

@pytest.fixture()
def checkout_page(logged_in_driver):
    # Returns Checkout Page
    return CheckoutPage(logged_in_driver)