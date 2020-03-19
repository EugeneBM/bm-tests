from src.automation_tests_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    __url = "https://www.blazemeter.com/"
    __startTestingNowButtonLocator = ".//button[@class='get_started_button home_get_started_button']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def startTestingNowButton(self):
        return BasePage.find_element(self, By.XPATH, self.__startTestingNowButtonLocator)

    def navigate(self):
        BasePage.navigate(self, self.__url)
