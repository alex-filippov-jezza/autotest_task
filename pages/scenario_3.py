from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os.path


class Scenario3Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def scroll_to_footer(self):
        footer = (By.CSS_SELECTOR, '#container > div.sbisru-Footer.sbisru-Footer__scheme--default > '
                                   'div.sbis_ru-container')
        return self.scroll_to(self.find(footer))

    @property
    def footer(self):

        f_element = (By.CSS_SELECTOR, '#container > div.sbisru-Footer.sbisru-Footer__scheme--default > '
                                      'div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > ul >'
                                      ' li:nth-child(8) > a')
        return self.find(f_element)

    def footer_click(self):
        return self.footer.click()

    @property
    def plugin(self):
        p_element = (
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')
        return self.find(p_element)

    def plugin_click(self):
        return self.plugin.click()

    def check_os(self):

        win_button = (By.XPATH, '//*[@id="ws-sqr8cgrnisr1713519115198"]/div[1]/div/div/span')
        if self.browser.current_url != 'https://sbis.ru/download?tab=plugin&innerTab=default':
            return self.find(win_button).click()
        else:
            return

    @property
    def download(self):
        download_element = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
        return self.find(download_element)

    def download_click(self):
        return self.download.click()

    @property
    def check_file(self):
        filename = "sbisplugin-setup-web.exe"
        if filename in os.listdir('.'):
            return True
        else:
            return False

    @property
    def check_file_size(self):
        file_size: float = round(os.path.getsize('sbisplugin-setup-web.exe') / 1048576, 2)
        return file_size
