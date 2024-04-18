from pages.scenario_2 import Scenario2Page
from pages.global_variable import sbis, link_tensor_about, link_tensor
from conftest import browser
from selenium.webdriver.common.action_chains import ActionChains


def test_scenario2(browser):
    scenario2 = Scenario2Page(browser)
    browser.implicitly_wait(10)
    scenario2.open(sbis)
    scenario2.contacts_open()
    region = scenario2.define_region()
    assert region == 'Ярославская обл.', "Регион - не Ярославская область"
    partners = scenario2.get_partners_list()
    assert partners is not None, "Список партнеров есть"
    scenario2.change_region()
    region_new = scenario2.define_region()
    assert region_new != region, "Регион не изменился"
    partners_new = scenario2.get_partners_list()
    assert partners_new != partners, "Список партнеров не изменился"


