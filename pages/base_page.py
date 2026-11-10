from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class BasePage:
    PATH = "/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.TIMEOUT)

    def open(self):
        self.driver.get(f"{settings.BASE_URL}{self.PATH}")
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator):
        return self.find(locator).text

    @property
    def current_path(self):
        return self.driver.current_url.removeprefix(settings.BASE_URL)
