from abc import *


class BasePage(metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)
