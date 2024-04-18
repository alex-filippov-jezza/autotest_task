from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class Scenario2Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_region(self):
        region = (By.CSS_SELECTOR, '#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > '
                                   'div.sbis_ru-container.sbisru-Contacts__relative > '
                                   'div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid'
                                   '-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > '
                                   'div:nth-child(2) > span > span')

        return self.find(region)

    def define_region(self):
        return self.find_region().text

    def get_partner(self, count: int):
        data_path = (By.XPATH,
                     f'//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[{count}]/div')

        name = self.find(data_path).text
        return name

    def get_partners_list(self):
        partners = []
        i = 1
        while i:
            try:
                partners.append(self.get_partner(i))
                i += 1
            except NoSuchElementException:
                break
        return partners

    def change_region(self):
        new_region = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
        self.find_region().click()
        return self.find(new_region).click()

    def get_url_title(self):
        title: str = self.browser.title
        url: str = self.browser.current_url

        if (title, url) == (
                'СБИС Контакты — Камчатский край', 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'):
            return True
        else:
            return False
