from src.automation_tests_ui.pages.home.home_page import HomePage
import logging


class HomePageTestContext:

    def __init__(self, driver):
        self.homePage = HomePage(driver)

    def navigate(self):
        logging.info("Go to Home page")
        self.homePage.navigate()

    def click_start_testing_button(self):
        logging.info("Click 'Start Testing Now' button")
        self.homePage.startTestingNowButton.click()
