from src.testframework_ui.selenium_driver import SeleniumDriver
from src.automation_tests_ui.pages.home.home_page import HomePage
import time
import pytest
import unittest


class TestBm(unittest.TestCase):
    seleniumDriver = None
    homePage = None

    def setup_class(self):
        self.seleniumDriver = SeleniumDriver()
        self.seleniumDriver.open()
        self.homePage = HomePage(self.seleniumDriver.driver)

    def teardown_class(self):
        self.seleniumDriver.close()

    def test_test1(self):
        self.seleniumDriver.navigate('https://www.www-bm-qa-base.blazemeter.net/')
        self.homePage.startTestingNowButton.click()
        time.sleep(5)
