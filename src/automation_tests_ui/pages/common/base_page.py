from abc import *
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def wait_for_page_load(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete')

    @property
    def url(self):
        return self.driver.current_url