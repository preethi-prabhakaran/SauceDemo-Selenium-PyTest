from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Base class with some common methods to be used for all page classes
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located(element_locator))
        return element

    def find_multiple_elements(self, element_locator):
        self.driver.find_element(element_locator)

    def click_on(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.element_to_be_clickable(element_locator))
        element.click()