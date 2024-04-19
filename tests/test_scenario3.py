from selenium.webdriver.common.by import By

from pages.scenario_3 import Scenario3Page
from pages.global_variable import sbis, link_tensor_about, link_tensor
from conftest import browser
import time
import os
import os.path


def test_scenario3(browser):
    scenario3 = Scenario3Page(browser)
    scenario3.open(sbis)
    scenario3.scroll_to_footer()
    scenario3.footer_click()
    time.sleep(5)
    scenario3.plugin_click()
    time.sleep(5)
    scenario3.check_os()
    scenario3.download_click()
    time.sleep(10)
    assert scenario3.check_file, "Файл не скачался"
    assert scenario3.check_file_size == 7.12, "Размер совпадает"

