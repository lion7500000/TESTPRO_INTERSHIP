from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchPage(Page):

    search_result = (By.XPATH, "//strong[text()='Ketsa']")
    search_artist = (By.XPATH, "//section[2]/ul/li/article/footer/div/a")
    sss = (By.XPATH, "//section[2]/p[text()='None found.']")

    def verify_search_text(self, text):
        self.verify_text(text, *self.search_result)

    def verify_artist_search_text(self, text):
        self.verify_text(text, *self.search_artist)

    def verify_artist_in_text(self, text):
        self.verify_found_text(text, *self.sss)


