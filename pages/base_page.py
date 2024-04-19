from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open(self, link: str):
        self.browser.get(link)

    def contacts_open(self):
        section_selector = (By.CSS_SELECTOR, '#wasaby-content > div > div > '
                                             'div.sbis_ru-Region.bodyContent__zIndex-context > div.sbis_ru-content > '
                                             'div.sbisru-Header-sticky.sbisru-Header--font.sbisru-Header__scheme'
                                             '--default > div.sbisru-Header > '
                                             'div.sbisru-Header__container.sbis_ru-container > ul > '
                                             'li.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid'
                                             '--hide-sm > a')
        self.find(section_selector).click()

    def scroll_to(self, block):
        action = ActionChains(self.browser)
        return action.move_to_element(block).perform()
