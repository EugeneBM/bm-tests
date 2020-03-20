from selenium.webdriver import Chrome
from src.testframework_ui.utils.config_parser import ConfigParser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverInitializer:
    __section = "BROWSERSETTINGS"

    def getDriver(self):
        settings = ConfigParser.get_settings()
        browser = settings.get(self.__section, "BrowserName")
        capabilities = DesiredCapabilities().CHROME
        capabilities['acceptSslCerts'] = True

        if browser == "Chrome":
            return Chrome(settings.get(self.__section, "DriversFolder") + "chromedriver.exe",
                          desired_capabilities=capabilities)
        else:
            raise Exception("{0} browser not implemented".format(browser))
