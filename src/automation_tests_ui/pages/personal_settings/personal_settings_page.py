from src.automation_tests_ui.pages.base_page import BasePage
from src.automation_tests_ui.pages.personal_settings.elements.edit_account_form import EditAccountForm
from selenium.webdriver.common.by import By


class PersonalSettingsPage(BasePage):

    __editAccountFormLocator = ".//div[@class='col-sm-9 content-area']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def editAccountForm(self):
        return EditAccountForm(self.driver.find_element(By.XPATH, self.__editAccountFormLocator))

