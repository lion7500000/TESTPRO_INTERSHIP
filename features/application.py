from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.playlist_page import PlaylistPage
from pages.profile_page import ProfilePage

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.playlist_page = PlaylistPage(self.driver)
        self.profile_page = ProfilePage(self.driver)


