from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    prefs = {"download.default_directory": r"C:\Users\alex2\PycharmProjects\autotest_task\tests\\", "safebrowsing"
                                                                                                    ".enabled": "true"}
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_browser = webdriver.Chrome(chrome_options)
    chrome_browser.implicitly_wait(10)

    return chrome_browser
