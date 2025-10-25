from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Page class for product details page, the page that appears on clicking a particular product from the listed page

class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.large_item_name = (By.CSS_SELECTOR, ".inventory_details_name.large_size")
        self.add_to_cart_locator = (By.ID, "add-to-cart")
        self.remove_button_locator = (By.ID, "remove")

    def name_check(self):
        element = self.find(self.large_item_name)
        return element.text

    def add_to_cart_details_page(self):
        self.click_on(self.add_to_cart_locator)

    def remove_button_present(self):
        remove = self.find(self.remove_button_locator)
        return remove.text