import subprocess
import time

import pytest
from selenium import webdriver

TEST_SERVER_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="module", autouse=True)
def server():
    server = subprocess.Popen(['python', '-m', 'flask_testing'])
    time.sleep(1)
    yield server
    server.terminate()


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.refresh()
    browser.quit()


def test_hello(browser):
    browser.get(TEST_SERVER_URL)
    body = browser.find_element_by_tag_name('body').text
    assert 'Hello World!' in body
