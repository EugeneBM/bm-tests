from selenium.webdriver import Chrome


class DriverInitializer:

    def getDriver(self):
        return Chrome('C:\\SeleniumDrivers\\chromedriver.exe')
