from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Page class for cart page

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_badge_locator = (By.CSS_SELECTOR, "span.shopping_cart_badge")
        self.cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_title_locator = (By.CSS_SELECTOR, "span.title")
        self.cart_item_locator = (By.CLASS_NAME, "cart_item")
        self.remove_locator_xpath = "//div[@class='inventory_item_name' and text()='{desired_product}']//parent::a//following-sibling::div/button"

    def click_on_cart(self):
        self.click_on(self.cart_locator)

    def items_in_cart_badge(self):
        return self.find(self.cart_badge_locator).text

    def cart_page_title(self):
        return self.find(self.cart_title_locator).text

    def count_items_in_cart(self):
        items = self.driver.find_elements(*self.cart_item_locator)
        return len(items)

    def remove_item_from_cart(self, product_name):
        self.click_on((By.XPATH, self.remove_locator_xpath.format(desired_product=product_name)))
