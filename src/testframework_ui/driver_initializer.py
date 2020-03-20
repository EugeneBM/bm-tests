from selenium.webdriver import Chrome
from src.testframework_ui.utils.config_parser import ConfigParser


class DriverInitializer:
    __section = "BROWSERSETTINGS"

    def getDriver(self):
        settings = ConfigParser.get_settings()
        browser = settings.get(self.__section, "BrowserName")

        if browser == "Chrome":
            return Chrome(settings.get(self.__section, "DriversFolder") + "chromedriver.exe")
        else:
            raise Exception("{0} browser not implemented".format(browser))