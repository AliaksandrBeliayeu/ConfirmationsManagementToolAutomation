"""
This module will contain regular fixtures. Like Set Up and Tear Down.
"""
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    #options = Options()
    #options.add_argument('--headless')
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
