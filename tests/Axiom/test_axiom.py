import pytest
from page_objects.Axiom.axiom_page import AxiomPage


class TestAxiom:
    @pytest.mark.debug
    def test_axiom(self, driver):
        axiom_page = AxiomPage(driver)
        axiom_page.open()
        axiom_page.accept_cookies()
        # axiom_page.close_popup()
        axiom_page.select_practice_areas()
        axiom_page.select_industries()
        axiom_page.save_solicitor()
        axiom_page.review_saved_solicitor()
        axiom_page.show_more_info()
        axiom_page.lets_talk()
