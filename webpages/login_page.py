"""
This page contains logging in logic.
"""
from webpages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    Login page class.
    """
    @classmethod
    def login(cls, browser):
        """
        A method for logging in.
        :param browser: A fixture will be put as an attribute.
        """
        browser.get(BasePage.base_url)
        email_text_field = BasePage.find_element((By.CSS_SELECTOR, '.form-control.ltr_override.input.ext-input.text-box.ext-text-box'), browser)
        email_text_field.send_keys('Aleksandr.Beliaev@royalmail.com')
        next_button = BasePage.find_element((By.CSS_SELECTOR, '.win-button'), browser)
        next_button.click()
        email_password_textfield = BasePage.find_element((By.CSS_SELECTOR, '#passwordInput'), browser)
        email_password_textfield.send_keys('ACDCDIO1aaaaaaaaaaa')
        next_button = BasePage.find_element((By.CSS_SELECTOR, '.submit'), browser)
        next_button.click()
        yes_button = BasePage.find_element((By.CSS_SELECTOR, '.win-button'), browser)
        yes_button.click()