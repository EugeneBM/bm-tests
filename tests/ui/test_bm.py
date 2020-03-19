from src.automation_tests_ui_business.test_contexts.home_page.home_page_test_context import HomePageTestContext
from tests.ui.test_base import BaseTestClass
import time


class TestBm(BaseTestClass):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        seleniumDriver = cls.seleniumDriver
        cls.homePageContext = HomePageTestContext(seleniumDriver.driver)

    def test_test1(self):
        self.homePageContext.navigate()
        self.homePageContext.click_start_testing_button()
        time.sleep(5)

    def test_test2(self):
        self.homePageContext.navigate()
        self.homePageContext.click_start_testing_button()
        time.sleep(5)
