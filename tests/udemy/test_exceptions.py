import pytest
from page_objects.udemy.exceptions_page import ExceptionsPage

class TestExceptions:
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_new_row(1)
        assert exceptions_page.is_row2_displayed, "Row 2 should be displayed but it is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_new_row(1)
        exceptions_page.add_new_food("Carrots", 1)
        assert exceptions_page.verify_text_confirmation_message() == "Row 2 was saved", ("Error: Confirmation Message "
                                                                                         "not as expected!")
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        new_food = "Pear"
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.edit_food_row_1(new_food, 10)
        assert exceptions_page.verify_text_confirmation_message() == "Row 1 was saved", ("Error: Confirmation Message "
                                                                                         "not as expected!")
    @pytest.mark.exceptions
    def test_state_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_new_row(1)
        assert not exceptions_page.is_instructions_visible(), "Error Instructions should no longer be visible"

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_new_row(1)
        assert exceptions_page.is_row2_displayed, "Row 2 input is not displayed!!"