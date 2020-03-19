from src.testframework_ui.selenium_driver import SeleniumDriver


class BaseTestClass:

    @classmethod
    def setup_class(cls):
        cls.seleniumDriver = SeleniumDriver()
        cls.seleniumDriver.open()

    @classmethod
    def teardown_class(cls):
        cls.seleniumDriver.close()
