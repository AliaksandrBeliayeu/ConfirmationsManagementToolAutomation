"""
This module contains logic for the Base Page of Confirmations Management Tool(CMT).
"""
from webpages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


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
        """
        title_element = cls.find_element((By.CSS_SELECTOR, '#name'), browser)
        title_element.click()
        title_element.send_keys(title)

    @classmethod
    def enter_subtitle(cls, browser, subtitle):
        """
        A method to hide finding 'Subtitle' element logic and enter the value of subtitle for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param subtitle: A variable for a subtitle of the created Confirmation
        """
        subtitle_element = cls.find_element((By.CSS_SELECTOR, '#subtitle'), browser)
        subtitle_element.click()
        subtitle_element.send_keys(subtitle)

    @classmethod
    def set_category_dropdown(cls, browser, category):
        """
        A method to hide finding 'Category' dropdown element logic and the value for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param category: A variable for a category of the created Confirmation, should be either 'Brief' or 'Message'.
        """
        dropdown_element = cls.find_element((By.CSS_SELECTOR, '#category'), browser)
        dropdown = Select(dropdown_element)
        if category == 'Brief':
            dropdown.select_by_visible_text('Brief')
        if category == 'Message':
            dropdown.select_by_visible_text('Message')

    @classmethod
    def set_priority_dropdown(cls, browser, priority):
        """
        A method to hide finding 'Priority' dropdown element logic and the value for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param priority: A variable for a category of the created Confirmation,
        should be either 'Low' or 'Medium' or 'High'.
        """
        dropdown_element = cls.find_element((By.CSS_SELECTOR, '#priority'), browser)
        dropdown = Select(dropdown_element)
        if priority == 'Low':
            dropdown.select_by_visible_text('Low')
        if priority == 'Medium':
            dropdown.select_by_visible_text('Medium')
        if priority == 'High':
            dropdown.select_by_visible_text('High')

    @classmethod
    def set_location(cls, browser, location):
        """
        A method to hide finding 'Location' dropdown/radiobutton element logic
        and the value for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param location: A variable for a location of the created Confirmation,
        should be either 'National' or 'ROD' or 'OPL' or 'DO'.
        """
        if location == 'National':
            pass  # This value should be pre-selected by default.
        else:
            specific_location_radiobutton = cls.find_element((By.CSS_SELECTOR, '.form-check:nth-child(2)'), browser)
            specific_location_radiobutton.click()
            if location == 'ROD':
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06D'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('ROD Anglia')
            if location == 'OPL':
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06D'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('ROD Anglia')
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06G'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('OPL Norwich and Ipswich North')
            if location == 'DO':
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06D'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('ROD Anglia')
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06G'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('OPL Norwich and Ipswich North')
                dropdown_element = cls.find_element((By.CSS_SELECTOR, '#0HN4FN9Q9E06J'), browser)
                dropdown = Select(dropdown_element)
                dropdown.select_by_visible_text('Acle SPDO')

    @classmethod
    def enter_date(cls, browser):
        """
        A method to hide finding 'Completion Date' element logic and enter the value for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        """
        date_element = cls.find_element((By.CSS_SELECTOR, '#expiryDate'), browser)
        date_element.click()
        current_date = datetime.now().strftime('%d/%m/%Y')
        date_element.send_keys(current_date)

    @classmethod
    def set_confirmation_text(cls, browser, text):
        """
        A method to hide finding 'Key Message' textfield element logic and the value for the created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        :param text: A variable for a 'Key Message' of the created Confirmation, should be either 'Brief' or 'Message'.
        """
        text_field = cls.find_element((By.CSS_SELECTOR, '.ql-editor.ql-blank'), browser)
        actions = ActionChains(browser)
        actions.move_to_element(text_field).perform()
        text_field.click()
        text_field.send_keys(text)

    @classmethod
    def publish_confirmation(cls, browser):
        """
        A method to hide finding 'Publish' button element logic and posting a created Confirmation.
        :param browser: WebDriver will be sent via fixture called browser.
        """
        button = cls.find_element((By.CSS_SELECTOR, 'button.btn.btn-primary[b-1fkzxkal6r]'), browser)
        actions = ActionChains(browser)
        actions.move_to_element(button).perform()
        button.click()


