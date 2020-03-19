from src.testframework_ui.selenium_driver import SeleniumDriver
from src.automation_tests_ui_business.test_contexts.home_page.home_page_test_context import HomePageTestContext
import time
import pytest
import unittest


class TestBm(unittest.TestCase):
    seleniumDriver = None
    homePage = None

    def setup_class(self):
        self.seleniumDriver = SeleniumDriver()
        self.seleniumDriver.open()
        self.homePageContext = HomePageTestContext(self.seleniumDriver.driver)

    def teardown_class(self):
        self.seleniumDriver.close()

    def test_test1(self):
        self.seleniumDriver.navigate('https://www.www-bm-qa-base.blazemeter.net/')
        self.homePageContext.click_start_testing_button()
        time.sleep(5)
