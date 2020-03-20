from src.automation_tests_ui.pages.welcome.welcome_page import WelcomePage
from src.automation_tests_ui_business.test_contexts.common.application_test_context import ApplicationBasePageTestContext
import logging


class WelcomePageTestContext(ApplicationBasePageTestContext):

    def __init__(self, driver):
        ApplicationBasePageTestContext.__init__(self, driver)
        self.welcomePage = WelcomePage(driver)

    def click_skip_wizard_link(self):
        logging.info("Click 'Skip Wizard' link")
        self.welcomePage.skipWizardLink.click()

    def get_current_url(self):
        return self.welcomePage.url

    def wait_for_page_loaded(self):
        self.welcomePage.wait_for_page_load(20)
