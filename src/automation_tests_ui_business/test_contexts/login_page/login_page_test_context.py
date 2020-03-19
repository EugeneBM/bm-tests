from src.automation_tests_ui.pages.login.login_page import LoginPage


class LoginPageTestContext:

    def __init__(self, driver):
        self.loginPage = LoginPage(driver)

    def register(self, firstName, lastName, email, company):
        self.loginPage.loginForm.firstNameInput.send_keys(firstName)
        self.loginPage.loginForm.lastNameInput.send_keys(lastName)
        self.loginPage.loginForm.emailInput.send_keys(email)
        self.loginPage.loginForm.companyInput.send_keys(company)
        self.loginPage.loginForm.registerButton.click()
