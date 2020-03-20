from src.testframework_ui.driver_initializer import DriverInitializer
from src.testframework_ui.utils.config_parser import ConfigParser


class SeleniumDriver:
    driver = None
    __section = "BROWSERSETTINGS"

    def open(self):
        settings = ConfigParser.get_settings()
        element_implicit_wait_timeout = settings.get(self.__section, "ElementImplicitWaitTimeout")
        page_load_timeout = settings.get(self.__section, "PageLoadTimeout")

        self.driver = DriverInitializer().getDriver()
        self.driver.set_page_load_timeout(int(page_load_timeout))
        self.driver.implicitly_wait(int(element_implicit_wait_timeout))
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def navigate(self, url):
        self.driver.get(url)
