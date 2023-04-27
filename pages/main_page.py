from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    email = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH, "//input[@type='password']")
    login = (By.XPATH, '//button[@type="submit"]')
    CREATE_PLAYLIST_BTN = (By.XPATH, '//i[@class="fa fa-plus-circle create"]')
    NEW_PLAYLIST_BTN = (By.XPATH, '//li[@data-testid="playlist-context-menu-create-simple"]')
    PLYLIST_FILD = (By.CSS_SELECTOR, 'input[name="name"]')
    LOGOUT_BTN = (By.XPATH, "//i[@class= 'fa fa-sign-out']")
    search_fild = (By.XPATH, "//input[@type='search']")
    search_artist = (By.XPATH, "//li/article[@title='Dan Brasco']")
    PLAY_MUISC_BTN = (By.XPATH, "//span[@title='Play or resume']")
    SONG_DARK_DAYS = (By.XPATH, "//ol[@class='recently-added-album-list']//article[@title='Dark Days EP by Grav']")
    TOGGLE_BTN = (By.XPATH, "//img[@alt='Sound bars']")

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def enter_email(self, text):
        self.input_text(text, *self.email)

    def enter_pw(self, text):
        self.input_text(text, *self.password)

    def click_LogIn_btn(self):
        self.click(*self.login)

    def verify_Logout_btn(self):
        self.wait_for_element_appear(*self.LOGOUT_BTN)

    def input_text_to_serch_fild(self, text):
        self.input_text(text, *self.search_fild)

    def clik_search_fild(self):
        self.click(*self.search_fild)

    def click_song(self):
        self.click(*self.SONG_DARK_DAYS)

    def move_mouse_click_play_btn(self):
        play_btn = self.find_element(*self.PLAY_MUISC_BTN)
        self.actions.move_to_element(play_btn).click().perform()

    def wait_for_sound_bar(self):
        self.wait_for_element_appear(*self.TOGGLE_BTN)

    def enter_search_text(self,text):
        self.input_text(text, *self.search_fild)






