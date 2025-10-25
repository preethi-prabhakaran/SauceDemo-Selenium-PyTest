from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Page class for products listing page

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.products_title = (By.CLASS_NAME, "title")
        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.inventory_item = (By.CLASS_NAME, "inventory_item")
        self.inventory_item_name = (By.CLASS_NAME, "inventory_item_name ")
        self.sort_field = (By.CLASS_NAME, "product_sort_container")
        self.sort_z_to_a = (By.CSS_SELECTOR, "span.select_container > select > option:nth-child(2)")
        self.product_xpath = "//div[@class='inventory_item_name ' and text()='{desired_product}']"
        self.add_to_cart_xpath = "//div[text()='{desired_product}']//ancestor::div[@class='inventory_item_label']//following-sibling::div//button"
        self.remove_locator_xpath = "//div[text()='{desired_product}']/ancestor::div[@class='inventory_item']//button[contains(@id, 'remove')]"

    def is_displayed(self):
        title_text = self.find(self.products_title).text
        return "Products" in title_text

    def get_products(self):
        products = self.driver.find_elements(*self.inventory_item_name)
        return products

    def product_list_is_displayed(self):
        products = self.get_products()
        return len(products)

    def get_product_names(self):
        products = self.get_products()
        return [prod.text for prod in products]

    def sort_name_z_to_a(self):
        #Find the sort field and click
        self.find(self.sort_field).click()

        # Click the option sort z to a from the dropdown
        self.find(self.sort_z_to_a).click()

    def add_to_cart_list_page(self, product_name):
        self.click_on((By.XPATH, self.add_to_cart_xpath.format(desired_product=product_name)))

    def click_on_product(self, product_name):
        self.click_on((By.XPATH, self.product_xpath.format(desired_product=product_name)))




