import subprocess
import time

import pytest
from selenium import webdriver

TEST_SERVER_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="module", autouse=True)
def server():
    print("Starting Server")
    server = subprocess.Popen(['python', '-m', 'flask_testing'])
    time.sleep(1)
    yield server
    print("Terminating Server")
    server.terminate()


@pytest.fixture()
def browser():
    print("Starting Browser")
    browser = webdriver.Firefox()
    print("Setting Implicit")
    browser.implicitly_wait(5)
    print("MAX Window")
    browser.maximize_window()
    yield browser
    print("Closing Browser")
    browser.refresh()
    browser.quit()


def test_hello(browser):
    browser.get(TEST_SERVER_URL)
    body = browser.find_element_by_tag_name('body').text
    assert 'Hello World!' in body
