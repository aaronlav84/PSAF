from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class AxiomPage(BasePage):
    __url = "https://www.axiomlaw.com/access-legal-talent"
    __accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    __close_popup_button = (By.XPATH,"//div[@class='leadin-close']")

    __practice_area1 = (By.XPATH, "(//div[@id='AccessLegalTalent']//div["
                                  "@class='CheckboxStyles__CheckboxContainer-sc-1u6u152-1 cUipLJ']/div["
                                  "@class='CheckboxStyles__CheckboxIconWrapper-sc-1u6u152-5 iyKcXb'])[2]")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def accept_cookies(self):
        super()._click(self.__accept_cookies_button)

    def close_popup(self):
        super()._click(self.__close_popup_button)

    def select_PA1(self):
        super()._scroll_500px()
        super()._wait_until_element_is_clickable(self.__practice_area1)
        super()._click(self.__practice_area1)
        # checkin test comment added
        # new branch, new commit and push