from src.testframework_ui.driver_initializer import DriverInitializer
from src.testframework_ui.utils.config_parser import ConfigParser
from datetime import datetime
import os


class SeleniumDriver:
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

    def take_screenshot(self, file):
        directory_name = "screenshots"
        root_dir = os.path.dirname(os.path.abspath(file))
        screenshot_path = os.path.join(os.path.sep, root_dir, directory_name)
        if not os.path.isdir(screenshot_path):
            os.mkdir(screenshot_path)
        name = datetime.now().strftime("%Y%m%d%H%M%S")
        self.driver.save_screenshot('{0}/{1}.png'.format(screenshot_path, name))
