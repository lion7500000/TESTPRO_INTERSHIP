from pages.main_page import MainPage
from pages.search_page import SearchPage

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)

