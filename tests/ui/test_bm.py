from src.testframework_ui.selenium_driver import SeleniumDriver
import time

class TestBm:
    driver = None

    def setup_class(self):
        self.driver = SeleniumDriver()
        self.driver.open()

    def teardown_class(self):
        self.driver.close()

    def test_test1(self):
        self.driver.navigate('https://github.com/')
        time.sleep(5)
