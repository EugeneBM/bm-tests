from selenium.webdriver.common.by import By


class EditAccountForm:
    __firstNameInputLocator = ".//input[@id='firstName']"
    __lastNameInputLocator = ".//input[@id='lastName']"
    __saveButtonLocator = ".//button[@class='btn btn-primary btn-lg']"
    __alertSuccessLocator = ".//div[@class='alert alert-success']"

    def __init__(self, parent):
        self.parent = parent

    @property
    def firstNameInput(self):
        return self.parent.find_element(By.XPATH, self.__firstNameInputLocator)

    @property
    def lastNameInput(self):
        return self.parent.find_element(By.XPATH, self.__lastNameInputLocator)

    @property
    def saveButton(self):
        return self.parent.find_element(By.XPATH, self.__saveButtonLocator)

    @property
    def alertSuccess(self):
        return self.parent.find_element(By.XPATH, self.__alertSuccessLocator)
