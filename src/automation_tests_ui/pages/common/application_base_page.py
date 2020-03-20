from automation_tests_ui.pages.common.base_page import BasePage
from src.automation_tests_ui.pages.common.elements.header import Header
from selenium.webdriver.common.by import By


class ApplicationBasePage(BasePage):
    __headerLocator = ".//bzm-header"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def header(self):
        root = BasePage.find_element(self, By.XPATH, self.__headerLocator)
        return Header(self.expand_shadow_element(root))

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
