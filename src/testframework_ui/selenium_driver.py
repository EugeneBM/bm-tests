from src.testframework_ui.driver_initializer import DriverInitializer


class SeleniumDriver:

    driver = None

    def open(self):
        self.driver = DriverInitializer().getDriver()
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def navigate(self, url):
        self.driver.get(url)
