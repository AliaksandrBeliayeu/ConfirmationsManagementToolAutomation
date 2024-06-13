"""
This module contains logic for the Base Page of Confirmations Management Tool(CMT).
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    """
    Class containing logic for initiating the base url of CMT and basic manipulations with all the pages.
    """
    #Initiating the base url.
    base_url = 'https://rmg-ne-cnf-dev-wa-01.azurewebsites.net/confirmations/'

    @classmethod
    def find_element(cls, locator, browser):
        """
        A method to hide WebDriverWait logic when finding an element on the page.
        :param browser: WebDriver will be sent via fixture called browser.
        :param locator: A locator of the searched element.
        """
        return WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator))

    @classmethod
    def go_to(cls, browser, url_modifier):
        """
        A method to initiate browser and navigate to the base URL + URL addition.
        e.g. 'https://rmg-ne-cnf-dev-wa-01.azurewebsites.net/confirmations/' + 'new' = 'https://rmg-ne-cnf-dev-wa-01.azurewebsites.net/confirmations/new'
        :param browser: WebDriver will be sent via fixture called browser.
        :param url_modifier: An addition to the Base URL to navigate to.
        """
        browser.get(f'{cls.base_url}' + f'{url_modifier}')





