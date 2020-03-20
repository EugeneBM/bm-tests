from src.automation_tests_ui.pages.login.login_page import LoginPage
import logging


class LoginPageTestContext:

    def __init__(self, driver):
        self.loginPage = LoginPage(driver)

    def register(self, firstName, lastName, email, company):
        logging.info("Enter First Name = '{0}'".format(firstName))
        self.loginPage.loginForm.firstNameInput.send_keys(firstName)

        logging.info("Enter Last Name = '{0}'".format(lastName))
        self.loginPage.loginForm.lastNameInput.send_keys(lastName)

        logging.info("Enter Email = '{0}'".format(email))
        self.loginPage.loginForm.emailInput.send_keys(email)

        logging.info("Enter Company = '{0}'".format(company))
        self.loginPage.loginForm.companyInput.send_keys(company)

        logging.info("Click 'Register' button")
        self.loginPage.loginForm.registerButton.click()

    def is_registration_form_displayed(self):
        return self.loginPage.loginForm.registerButton.is_displayed()
