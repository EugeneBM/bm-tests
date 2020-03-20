from src.automation_tests_ui.pages.common.application_base_page import ApplicationBasePage
import logging


class ApplicationBasePageTestContext:

    def __init__(self, driver):
        self.applicationBasePage = ApplicationBasePage(driver)

    def click_profile_link(self):
        logging.info("Click 'Profile Menu' link")
        self.applicationBasePage.header.profileLink.click()

    def open_profile_settings(self):
        self.click_profile_link()
        logging.info("Click 'Personal Settings' link")
        self.applicationBasePage.header.profileMenu.profileSettingsLink.click()
