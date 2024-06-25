"""
This module will have the exact tests that will be testing an E2E scenario of Creating different types of Confirmations
AND automating creating of these confirmations to save time in future iterations.
"""
from webpages.login_page import LoginPage
from webpages.new_confirmation_page import NewConfirmationPage
import pytest
import time


class TestNationalConfirmationCreation(NewConfirmationPage):
    @staticmethod
    def test_logging_in(browser):
        LoginPage.login(browser)
        NewConfirmationPage.go_to(browser, NewConfirmationPage.url_modifier)

    @staticmethod
    def test_create_confirmation_title(browser):
        NewConfirmationPage.enter_title(browser, 'National Message High Confirmation Title')

    @staticmethod
    def test_create_confirmation_subtitle(browser):
        NewConfirmationPage.enter_subtitle(browser, 'National Message High Confirmation Subtitle')

    @staticmethod
    def test_set_category(browser):
        NewConfirmationPage.set_category_dropdown(browser, category='Message')

    @staticmethod
    def test_set_priority(browser):
        NewConfirmationPage.set_priority_dropdown(browser, priority='High')

    @staticmethod
    def test_set_location(browser):
        NewConfirmationPage.set_location(browser, location='National')

    @staticmethod
    def test_set_date(browser):
        NewConfirmationPage.enter_date(browser)

    @staticmethod
    def test_add_text_message(browser):
        NewConfirmationPage.set_confirmation_text(browser, text='This is a text for the Confirmation to be published.')

    @staticmethod
    def test_publish_confirmation(browser):
        NewConfirmationPage.publish_confirmation(browser)
        time.sleep(10)  # Time needed for the confirmation to be finalized and created.

if __name__ == '__main__':
    pytest.main()

