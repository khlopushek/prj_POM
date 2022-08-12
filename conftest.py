import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language: en or fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()

