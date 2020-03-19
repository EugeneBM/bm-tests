from src.automation_tests_ui_business.test_contexts.home_page.home_page_test_context import HomePageTestContext
from tests.ui.test_base import BaseTestClass
import time


class TestBm(BaseTestClass):

    def test_test1(self):
        seleniumDriver = self.seleniumDriver
        self.homePageContext = HomePageTestContext(seleniumDriver.driver)
        seleniumDriver.navigate('https://www.www-bm-qa-base.blazemeter.net/')
        self.homePageContext.click_start_testing_button()
        time.sleep(5)
