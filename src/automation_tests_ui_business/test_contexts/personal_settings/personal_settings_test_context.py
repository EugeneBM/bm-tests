from src.automation_tests_ui.pages.personal_settings.personal_settings_page import PersonalSettingsPage
from src.automation_tests_ui_business.test_contexts.common.application_test_context import \
    ApplicationBasePageTestContext
import logging


class PersonalSettingsTestContext(ApplicationBasePageTestContext):

    def __init__(self, driver):
        ApplicationBasePageTestContext.__init__(self, driver)
        self.personalSettingsPage = PersonalSettingsPage(driver)

    def enter_first_name(self, first_name):
        self.personalSettingsPage.editAccountForm.firstNameInput.clear()
        logging.info("Enter First Name = '{0}'".format(first_name))
        self.personalSettingsPage.editAccountForm.firstNameInput.send_keys(first_name)

    def enter_last_name(self, last_name):
        self.personalSettingsPage.editAccountForm.lastNameInput.clear()
        logging.info("Enter Last Name = '{0}'".format(last_name))
        self.personalSettingsPage.editAccountForm.lastNameInput.send_keys(last_name)

    def click_save_button(self):
        logging.info("Click 'Save' button")
        self.personalSettingsPage.editAccountForm.saveButton.click()

    def update_user_information(self, firs_name='', last_name='', email=''):
        if firs_name != '':
            self.enter_first_name(firs_name)

        if last_name != '':
            self.enter_last_name(last_name)

        self.click_save_button()

    def is_user_information_updated(self):
        return self.personalSettingsPage.editAccountForm.alertSuccess.is_displayed()
