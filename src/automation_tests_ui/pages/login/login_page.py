from src.automation_tests_ui.pages.common.base_page import BasePage
from src.automation_tests_ui.pages.login.elements.login_form import LoginForm
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    __loginFormLocator = ".//form[@id='kc-register-form']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def loginForm(self):
        return LoginForm(self.driver.find_element(By.XPATH, self.__loginFormLocator))

