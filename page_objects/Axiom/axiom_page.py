from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class AxiomPage(BasePage):
    __url = "https://www.axiomlaw.com/access-legal-talent"
    __accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    __close_popup_button = (By.XPATH, "//div[@class='leadin-close']")

    __practice_area_1 = (By.XPATH, "(//div[@id='AccessLegalTalent']//div["
                                   "@class='CheckboxStyles__CheckboxContainer-sc-1u6u152-1 cUipLJ']/div["
                                   "@class='CheckboxStyles__CheckboxIconWrapper-sc-1u6u152-5 iyKcXb'])[1]")

    __practice_area_2 = (By.XPATH, "(//div[@id='AccessLegalTalent']//div["
                                   "@class='CheckboxStyles__CheckboxContainer-sc-1u6u152-1 cUipLJ']/div["
                                   "@class='CheckboxStyles__CheckboxIconWrapper-sc-1u6u152-5 iyKcXb'])[2]")

    __practice_area_3 = (By.XPATH, "(//div[@id='AccessLegalTalent']//div["
                                   "@class='CheckboxStyles__CheckboxContainer-sc-1u6u152-1 cUipLJ']/div["
                                   "@class='CheckboxStyles__CheckboxIconWrapper-sc-1u6u152-5 iyKcXb'])[3]")

    __practice_area_4 = (By.XPATH, "(//div[@id='AccessLegalTalent']//div["
                                   "@class='CheckboxStyles__CheckboxContainer-sc-1u6u152-1 cUipLJ']/div["
                                   "@class='CheckboxStyles__CheckboxIconWrapper-sc-1u6u152-5 iyKcXb'])[4]")

    __industry_1 = (By.XPATH, "//div[@class='card-section-container background-light']//div[2]//div[2]//div[1]//div["
                              "1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]")

    __industry_2 = (By.XPATH, "//div[@class='card-section-container background-light']//div[2]//div[2]//div[1]//div["
                              "1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]")

    __industry_3 = (By.XPATH, "//div[@class='card-section-container background-light']//div[2]//div[2]//div[1]//div["
                              "1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]")

    __industry_4 = (By.XPATH, "//div[@class='card-section-container background-light']//div[2]//div[2]//div[1]//div["
                              "1]//div[1]//div[4]//div[1]//div[1]//div[1]//div[1]//div[1]")

    __save_button_1 = (By.XPATH, "//div[@class='content-wrapper']//div[3]//div[1]//div[1]//div[2]//div[1]//div["
                                 "1]//button[1]")

    __saved_solicitors = (By.XPATH, "//div[@id='AccessLegalTalent']//div[@class='hubspot-inject-shell']//div["
                                    "@class='InjectShell__Wrapper-sc-14ei2ur-0 kLqBzJ']//div["
                                    "@class='tabs-container']/div[2]//span[@class='tab-label-text']/span[.='Saved']")

    __show_more_information = (By.XPATH, "//div[@class='brief-control-button position-center']//button["
                                         "@type='button'][normalize-space()='Show More']")

    __lets_talk = (By.XPATH, "/html//div[@id='AccessLegalTalent']/div[@class='hubspot-inject-shell']//div["
                             "@class='InjectShell__Wrapper-sc-14ei2ur-0 kLqBzJ']/div[@class='content-wrapper']/div["
                             "@class='StoreStateTreatmentStyles__StoreStateTreatmentWrapper-sc-gs6hat-0 hdkrsc']/div["
                             "@class='StoreStateTreatmentStyles__StoreStateTreatmentWrapper-sc-gs6hat-0 "
                             "kZtgQM']/div/div//div[@class='TalentSearchStyles__TalentSearchWrapper-sc-1p62fji-1 "
                             "hYXKMj']/div[2]/div[2]/div/div/div/div/div[2]/button[@type='button']")

    __tell_us_more_locator = (By.XPATH, "/html/body/div[11]/div[@name='INQUIRE_WITH_AXIOM_FORM']/div[2]/div/div["
                                            "2]/div/div["
                                            "1]/div[@class='column']/div//div[@role='textbox']")

    __cover_letter_text = ("Hi there, I need a solicitor who is qualified in both UK and Northern Ireland in Copyright "
                           "and Patent law. I will need you to start from the 1st of November 2023 for 1 month. "
                           "Please send me details of your fees if you are able to work with these dates. Thanks and "
                           "Kind Regards.")

    __first_name_locator = (
        By.XPATH, "/html/body/div[11]/div[@name='INQUIRE_WITH_AXIOM_FORM']/div[2]/div/div[2]/div/div["
                  "2]/div[1]/div//input[@name='firstName']")

    __last_name_locator = (
        By.XPATH, "/html/body/div[11]/div[@name='INQUIRE_WITH_AXIOM_FORM']/div[2]/div/div[2]/div/div["
                  "2]/div[2]/div//input[@name='lastName']")

    __business_email_locator = (
        By.XPATH, "/html/body/div[11]/div[@name='INQUIRE_WITH_AXIOM_FORM']/div[2]/div/div[2]/div/div["
                  "3]/div[1]/div//input[@name='email']")

    __phone_number_locator = (
        By.XPATH, "/html/body/div[11]/div[@name='INQUIRE_WITH_AXIOM_FORM']/div[2]/div/div[2]//input["
                  "@name='phoneNumber']")

    __first_name = "Aaron"
    __last_name = "Lavery"
    __email = "aaron.lavery@abc.com"
    __phone_number = "07446770576"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def accept_cookies(self):
        super()._click(self.__accept_cookies_button)

    def close_popup(self):
        super()._click(self.__close_popup_button)

    def select_practice_areas(self):
        super()._scroll_500px()
        super()._wait_until_element_is_clickable(self.__practice_area_1)
        super()._click(self.__practice_area_1)
        super()._click(self.__practice_area_2)
        super()._click(self.__practice_area_3)
        super()._click(self.__practice_area_4)

    def select_industries(self):
        super()._scroll_500px()
        super()._click(self.__industry_1)
        super()._click(self.__industry_2)
        super()._click(self.__industry_3)
        super()._click(self.__industry_4)

    def save_solicitor(self):
        super()._click(self.__save_button_1)

    def review_saved_solicitor(self):
        super()._click(self.__saved_solicitors)

    def show_more_info(self):
        super()._click(self.__show_more_information)

    def lets_talk(self):
        super()._click(self.__lets_talk)
        super()._click(self.__tell_us_more_locator)
        super()._type(self.__tell_us_more_locator, self.__cover_letter_text)
        super()._type(self.__first_name_locator, self.__first_name)
        super()._type(self.__last_name_locator, self.__last_name)
        super()._type(self.__business_email_locator, self.__email)
        super()._type(self.__phone_number_locator, self.__phone_number)
