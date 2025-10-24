from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.log_btn_locator = (By.ID, "login-button")
        self.products_title = (By.CLASS_NAME, "title")

    def login(self, creds):
        self.find(self.username_locator).send_keys(creds[0])
        self.find(self.password_locator).send_keys(creds[1])
        self.find(self.log_btn_locator).click()

    def get_error_message(self):
        return self.find((By.XPATH, "//h3")).text

    def get_page_title(self):
        return self.find(self.products_title).text