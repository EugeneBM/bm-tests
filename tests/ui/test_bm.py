from src.automation_tests_ui_business.test_contexts.home_page.home_page_test_context import HomePageTestContext
from src.automation_tests_ui_business.test_contexts.login_page.login_page_test_context import LoginPageTestContext
from src.automation_tests_ui_business.test_contexts.welcome_page.welcome_page_test_context import WelcomePageTestContext
from src.automation_tests_ui_business.test_contexts.welcome_screen.welcome_screen_test_context import \
    WelcomeScreenPageTestContext
from src.automation_tests_ui_business.test_contexts.personal_settings.personal_settings_test_context import \
    PersonalSettingsTestContext
from tests.ui.test_base import BaseTestClass
from datetime import datetime


class TestBm(BaseTestClass):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        seleniumDriver = cls.seleniumDriver
        cls.homePageContext = HomePageTestContext(seleniumDriver.driver)
        cls.loginPageTestContext = LoginPageTestContext(seleniumDriver.driver)
        cls.welcomePageTestContext = WelcomePageTestContext(seleniumDriver.driver)
        cls.welcomeScreenPageTestContext = WelcomeScreenPageTestContext(seleniumDriver.driver)
        cls.personalSettingsTestContext = PersonalSettingsTestContext(seleniumDriver.driver)

    def test_user_registration(self):
        suffix = datetime.now().strftime("%Y%m%d%H%M%S")
        first_name = "fn" + suffix
        last_name = "ln" + suffix
        email = str.format("test_{0}@blazemeter.com", suffix)
        company = "company"

        self.homePageContext.navigate()
        self.homePageContext.click_start_testing_button()

        assert self.loginPageTestContext.is_registration_form_displayed()

        self.loginPageTestContext.register(first_name, last_name, email, company)
        self.welcomeScreenPageTestContext.wait_for_page_loaded()
        actualUrl = self.welcomePageTestContext.get_current_url()

        assert actualUrl.endswith('/welcome-wizard/http')

        self.welcomePageTestContext.click_skip_wizard_link()
        self.welcomePageTestContext.open_profile_settings()
        self.personalSettingsTestContext.update_user_information("newFirstName", "newLastName")

        assert self.personalSettingsTestContext.is_user_information_updated()
