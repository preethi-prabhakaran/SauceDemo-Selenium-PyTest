from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located(element_locator))
        return element

    def find_multiple_elements(self):
        self.driver.find_elements()

    def click_on(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.element_to_be_clickable(element_locator))
        element.click()