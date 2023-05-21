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
    HOME_BTN = (By.CSS_SELECTOR, "a.home.active")
    USER_PROFILE = (By.XPATH, "//a[@title='View/edit user profile']")
    PROFILE_EMAIL_FILD = (By.CSS_SELECTOR, "input#inputProfileEmail")
    PROFILE_SAVE_BTN = (By.XPATH, "//button[@class='btn-submit']")
    CURRENT_PASSWORD_FILD = (By.XPATH, "//input[@name='current_password']")
    NEW_PASSWORD_FILD = (By.XPATH, "//input[@name='new_password']")
    NOT_LOGIN_STATUS = (By.CSS_SELECTOR, "#nprogress")

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

    def verify_Home_btn(self):
        self.wait_for_element_appear(*self.HOME_BTN)

    def input_text_to_serch_fild(self, text):
        self.input_text(text, *self.search_fild)

    def input_curr_password_to_pass_fild(self, password):
        self.input_text(password, *self.CURRENT_PASSWORD_FILD)

    def input_new_password_to_pass_fild(self, password):
        self.input_text(password, *self.NEW_PASSWORD_FILD)

    def clik_search_fild(self):
        self.click(*self.search_fild)

    def click_song(self):
        self.click(*self.SONG_DARK_DAYS)

    def click_to_user_profile(self):
        self.click(*self.USER_PROFILE)

    def click_to_profile_save_btn(self):
        self.click(*self.PROFILE_SAVE_BTN)

    def click_to_logout_btn(self):
        self.click(*self.LOGOUT_BTN)

    def update_user_email(self, email):
        self.input_text(email, *self.PROFILE_EMAIL_FILD)

    def move_mouse_click_play_btn(self):
        play_btn = self.find_element(*self.PLAY_MUISC_BTN)
        self.actions.move_to_element(play_btn).click().perform()

    def wait_for_status_appear(self):
        self.wait_for_element_appear(*self.NOT_LOGIN_STATUS)

    def enter_search_text(self,text):
        self.input_text(text, *self.search_fild)

    def wait_for_element_activ(self):
        self.wait_for_element_click(*self.login)






