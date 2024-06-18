"""
This module will have the exact tests that will be testing an E2E scenario of Creating different types of Confirmations
AND automating creating of these confirmations to save time in future iterations.
"""
import time
from webpages.login_page import LoginPage
from webpages.new_confirmation_page import NewConfirmationPage



def test_create_confirmation(browser):
    LoginPage.login(browser)
    NewConfirmationPage.go_to(browser, NewConfirmationPage.url_modifier)
    NewConfirmationPage.enter_title(browser, 'Title for a Confirmation!')
    time.sleep(10)


if __name__ == '__main__':
    pytest.main()