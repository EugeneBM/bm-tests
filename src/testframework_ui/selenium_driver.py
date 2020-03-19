from src.testframework_ui.driver_initializer import DriverInitializer


class SeleniumDriver:

    driver = None

    def open(self):
        self.driver = DriverInitializer().getDriver()
        self.driver.set_page_load_timeout(15)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def navigate(self, url):
        self.driver.get(url)
