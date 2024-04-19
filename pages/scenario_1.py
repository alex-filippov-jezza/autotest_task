from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Scenario1Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def banner(self):
        banner_selector = (By.CSS_SELECTOR, '#contacts_clients > div.sbis_ru-container > div > div > '
                                            'div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 > div > a > img')
        return self.find(banner_selector)

    def banner_click(self):
        self.banner.click()

    def switch_tab(self):
        original_window = self.browser.current_window_handle

        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                return self.browser.switch_to.window(window_handle)

    @property
    def find_block(self):
        block_selector = (
            By.CSS_SELECTOR,
            '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > '
            'div:nth-child(1) > div')
        return self.find(block_selector)

    @property
    def block_is_displayed(self):
        return self.find_block.is_displayed()

    @property
    def about(self):
        link_selector = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
        return self.find(link_selector)

    def about_click(self):
        self.about.click()

    @property
    def current_url_page(self):
        return self.browser.current_url

    @property
    def working_section(self):

        working = (By.CSS_SELECTOR, '#container > div.tensor_ru-content_wrapper > div > '
                                    'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
        return self.find(working)

    def get_image_size(self, count: int):
        image_selector = (By.XPATH,
                          f'//*[@id="container"]/div[1]/div/div[4]/div[2]/div[{count}]/a/div[1]/img')
        sizes = self.find(image_selector).size
        w_h = sizes['width'], sizes['height']
        return w_h

    @property
    def compare_images_result(self):
        k = 0
        for i in range(1, 4):
            size1 = self.get_image_size(i)
            size2 = self.get_image_size(i + 1)
            if size1 == size2:
                k += 1

        if k == 3:
            return k
        else:
            return None
