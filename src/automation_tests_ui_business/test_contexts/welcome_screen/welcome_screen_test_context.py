from src.automation_tests_ui.pages.welcome_screen.welcome_screen_page import WelcomeScreenPage


class WelcomeScreenPageTestContext:

    def __init__(self, driver):
        self.welcomeScreenPage = WelcomeScreenPage(driver)

    def wait_for_page_loaded(self):
        self.welcomeScreenPage.wait_for_page_load(20)
