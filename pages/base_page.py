from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_method(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_method(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def navigate_url_method(self, data_url):
        self.driver.get(data_url)

    def wait_url_to_be_visible_method(self, constants_url):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(constants_url))

    def wait_element_to_be_visible_method(self, locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def get_current_url_method(self):
        return self.driver.current_url

    def element_is_displayed_method(self, locator):
        return self.driver.find_element(*locator).is_displayed()