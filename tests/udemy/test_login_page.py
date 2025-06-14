import pytest

from page_objects.udemy.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.udemy.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "URL is not as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header not displayed"
        assert logged_in_page.is_logout_button_displayed(), "Logout button is not displayed"
