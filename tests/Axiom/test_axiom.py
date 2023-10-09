import pytest
from page_objects.Axiom.axiom_page import AxiomPage

class TestAxiom:
    @pytest.mark.debug
    def test_axiom(self, driver):
        axiom_page = AxiomPage(driver)
        axiom_page.open()
        axiom_page.accept_cookies()
#        axiom_page.close_popup()
        axiom_page.select_PA1()
