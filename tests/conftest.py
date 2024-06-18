"""
This module will contain regular fixtures. Like Set Up and Tear Down.
"""
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
