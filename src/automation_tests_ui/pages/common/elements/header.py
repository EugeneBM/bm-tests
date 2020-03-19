from selenium.webdriver.common.by import By
from src.automation_tests_ui.pages.common.elements.profile_menu import ProfileMenu


class Header:

    __profileLinkLocator = "dropdown-menu"
    __profileMenuLocator = "dropdown-content"

    def __init__(self, parent):
        self.parent = parent

    @property
    def profileLink(self):
        return self.parent.find_element(By.CLASS_NAME, self.__profileLinkLocator)

    @property
    def profileMenu(self):
        return ProfileMenu(self.parent.find_element(By.CLASS_NAME, self.__profileMenuLocator))
