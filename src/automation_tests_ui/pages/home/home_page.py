from src.automation_tests_ui.pages.common.base_page import BasePage
from selenium.webdriver.common.by import By
from src.testframework_ui.utils.config_parser import ConfigParser


class HomePage(BasePage):
    __section = "DEFAULT"
    __startTestingNowButtonLocator = ".//button[@class='get_started_button home_get_started_button']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def startTestingNowButton(self):
        return self.driver.find_element(By.XPATH, self.__startTestingNowButtonLocator)

    def navigate(self):
        settings = ConfigParser.get_settings()
        base_url = settings.get(self.__section, "BaseUrl")

        super().navigate(base_url)
