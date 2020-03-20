from src.testframework_ui.selenium_driver import SeleniumDriver
import logging
from src.testframework_ui.utils.config_parser import ConfigParser


class BaseTestClass:
    logging.basicConfig(filename='logs.log', level=ConfigParser.get_settings().get("LOGGER", "Loglevel"))
    logging.FileHandler(filename='logs.log', mode='w')

    @classmethod
    def setup_class(cls):
        cls.seleniumDriver = SeleniumDriver()
        cls.seleniumDriver.open()

    @classmethod
    def teardown_class(cls):
        cls.seleniumDriver.close()

    def teardown_method(self):
        self.seleniumDriver.take_screenshot(__file__)
