from abc import *
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def navigate(self, url):
        self.driver.get(url)

    def wait_for_page_load(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete')

    def get_title(self):
        return self.driver.title

    @property
    def url(self):
        return self.driver.current_url
