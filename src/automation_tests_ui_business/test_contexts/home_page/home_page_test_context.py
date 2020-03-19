from src.automation_tests_ui.pages.home.home_page import HomePage


class HomePageTestContext:

    def __init__(self, driver):
        self.homePage = HomePage(driver)

    def click_start_testing_button(self):
        self.homePage.startTestingNowButton.click()
