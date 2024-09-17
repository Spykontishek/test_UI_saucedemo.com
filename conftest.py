import pytest
from selenium import webdriver
from data import Data

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()

    browser.get(Data.URL)
    yield browser
    browser.quit()