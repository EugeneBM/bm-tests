from selenium.webdriver.common.by import By


class ProfileMenu:

    __personalSettingsLinkLocator = ".//li[1]/a"

    def __init__(self, parent):
        self.parent = parent

    @property
    def personalSettingsLink(self):
        return self.parent.find_element(By.XPATH, self.__personalSettingsLinkLocator)