import pytest
from selenium import webdriver


@pytest.fixture()
def setUp():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

