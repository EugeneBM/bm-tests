from automation_tests_ui.pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class WelcomePage(BasePage):

    __skipWizardLinkLocator = ".//a[@class='skip']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def skipWizardLink(self):
        return BasePage.find_element(self, By.XPATH, self.__skipWizardLinkLocator)