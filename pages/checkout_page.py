from selenium.webdriver.common.by import By
from config.config_reader import first_name, last_name, postal_code
from pages.base_page import BasePage

# Page class for checkout page
class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_locator = (By.ID, "checkout")
        self.title_locator = (By.CLASS_NAME, "title")
        self.first_name_locator = (By.ID, "first-name")
        self.last_name_locator = (By.ID, "last-name")
        self.postal_code_locator = (By.ID, "postal-code")
        self.continue_locator = (By.ID, "continue")
        self.total_summary_locator = (By.CLASS_NAME, "summary_total_label")
        self.finish_locator = (By.ID, "finish")
        self.burger_menu_locator = (By.CLASS_NAME, "bm-burger-button")
        self.logout_locator = (By.LINK_TEXT, "Logout")

    def checkout(self):
        self.click_on(self.checkout_locator)

    def checkout_page_title(self):
        return self.find(self.title_locator).text

    def fill_checkout_form(self):
        self.find(self.first_name_locator).send_keys(first_name())
        self.find(self.last_name_locator).send_keys(last_name())
        self.find(self.postal_code_locator).send_keys(postal_code())
        self.click_on(self.continue_locator)

    def price_summary_displayed(self):
        price_element = self.find(self.total_summary_locator)
        return price_element.is_displayed()

    def click_finish(self):
        self.click_on(self.finish_locator)

    def click_burger_menu(self):
        self.click_on(self.burger_menu_locator)

    def logout(self):
        self.click_on(self.logout_locator)
