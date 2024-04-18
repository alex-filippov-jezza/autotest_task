from pages.scenario_1 import Scenario1Page
from pages.global_variable import sbis, link_tensor_about, link_tensor
from conftest import browser
from selenium.webdriver.common.action_chains import ActionChains


def test_scenario1(browser):
    scenario1 = Scenario1Page(browser)
    scenario1.open(sbis)
    scenario1.contacts_open()
    scenario1.banner_click()
    scenario1.switch_tab()
    scenario1.scroll_to(scenario1.find_block)
    assert scenario1.block_is_displayed, "Блок <<Сила в людях>> отсутствует"
    scenario1.about_click()
    assert link_tensor_about == scenario1.current_url_page, "Открыт не https://tensor.ru/about"
    scenario1.scroll_to(scenario1.working_section)
    assert scenario1.compare_images_result == 3, "Размер изображений в разделе не одинаковый"

