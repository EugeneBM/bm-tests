from selenium.webdriver.common.by import By


class Header:

    __profileLinkLocator = "dropdown-menu"

    def __init__(self, parent):
        self.parent = parent

    @property
    def profileLink(self):
        return self.parent.find_element(By.CLASS_NAME, self.__profileLinkLocator)
