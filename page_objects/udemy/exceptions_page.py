from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __row1_input = (By.XPATH, "//div[@id='row1']/input")
    __row2_input = (By.XPATH, "//div[@id='row2']/input")
    __row1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __row1_edit_button = (By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    __row2_edit_button = (By.XPATH, "//div[@id='row2']/button[@name='Edit']")
    __add_button = (By.XPATH, "//button[@id='add_btn']")
    __instructions_text = (By.ID, "instructions")
    __confirmation_text = (By.ID, "confirmation")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_new_row(self, timeout: int):
        super()._click(self.__add_button, timeout)
        super()._wait_until_element_is_visible(self.__row2_input)

    def is_row2_displayed(self) -> bool:
        return super()._wait_until_element_is_visible(self.__row2_input)

    def type_into_row1_input(self, text: str, time: int):
        super()._type(self.__row1_input, text, time)

    def add_new_food(self, text: str, time: int):
        super()._type(self.__row2_input, text, time)
        super()._click(self.__row2_save_button)

    def edit_food_row_1(self, text: str, time: int):
        super()._wait_until_element_is_clickable(self.__row1_edit_button)
        super()._click(self.__row1_edit_button)
        super()._clear_text(self.__row1_input)
        super()._type(self.__row1_input, text, time)
        super()._click(self.__row1_save_button)

    def verify_text_confirmation_message(self) -> str:
        super()._wait_until_element_is_visible(self.__confirmation_text)
        return super()._get_text(self.__confirmation_text)

    def change_food(self):
        super()._clear_text(self.__row1_input)

    def get_input_1_text(self) -> str:
        return (super()._get_text(self.__row1_input))

    def wait_until_text_1_clickable(self):
        super()._wait_until_element_is_clickable(self.__row1_input)

    def wait_until_text_1_visible(self):
        super()._wait_until_element_is_visible(self.__row1_input)

    def wait_until_instuctions_visible(self, time:int):
        super()._wait_until_element_is_visible(self.__instructions_text, time)

    def is_instructions_visible(self) -> bool:
        return super()._is_displayed(self.__instructions_text)
