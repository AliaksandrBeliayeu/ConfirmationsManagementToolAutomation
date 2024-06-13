"""
This module contains logic for the Base Page of Confirmations Management Tool(CMT).
"""
from webpages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewConfirmationPage(BasePage):
    """
    Class containing logic for initiating the base url of CMT and basic manipulations with all the pages.
    """
    # Initiating a modifier of the URL that will be added to the BaseURL from BasePage class.
    url_modifier = '/new'

    @classmethod
    def enter_title(cls, browser, title):
        """
        A method to hide finding 'Title' element logic and enter the value of Title for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param title: A variable for a Title of the created Confirmation
        :return:
        """
        title_element = cls.find_element((By.CSS_SELECTOR, '#name'), browser)
        title_element.click()
        title_element.send_keys(title)


