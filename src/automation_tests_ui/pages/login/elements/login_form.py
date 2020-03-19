from selenium.webdriver.common.by import By


class LoginForm:
    __firstNameInputLocator = ".//input[@id='firstName']"
    __lastNameInputLocator = ".//input[@id='lastName']"
    __emailInputLocator = ".//input[@id='email']"
    __companyInputLocator = ".//input[@id='user.attributes.company']"
    __registerButtonLocator = ".//input[@class='rounded btn btn-primary btn-block btn-lg']"

    def __init__(self, parent):
        self.parent = parent

    @property
    def firstNameInput(self):
        return self.parent.find_element(By.XPATH, self.__firstNameInputLocator)

    @property
    def lastNameInput(self):
        return self.parent.find_element(By.XPATH, self.__lastNameInputLocator)

    @property
    def emailInput(self):
        return self.parent.find_element(By.XPATH, self.__emailInputLocator)

    @property
    def companyInput(self):
        return self.parent.find_element(By.XPATH, self.__companyInputLocator)

    @property
    def registerButton(self):
        return self.parent.find_element(By.XPATH, self.__registerButtonLocator)
