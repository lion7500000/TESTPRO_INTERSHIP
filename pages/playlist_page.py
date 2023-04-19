from pages.base_page import Page
from selenium.webdriver.common.by import By

class PlaylistPage(Page):

    CREATE_PLAYLIST_BTN = (By.XPATH, "//i[@class='fa fa-plus-circle create']")
    NEW_PLAYLIST_BTN = (By.XPATH, '//li[@data-testid="playlist-context-menu-create-simple"]')
    SMART_PLAYLIST_MENU = (By.XPATH, "//li[@data-testid = 'playlist-context-menu-create-smart']")
    SMART_PL_NAME_FIL = (By.CSS_SELECTOR, "input[name='name']")
    SMART_PL_MODEL_FILD = (By.XPATH,"//select[@name='model[]']/option[text()='Title']")
    SMART_PL_OPERATOR_FILD = (By.XPATH, "//select[@name='operator[]']/option[text()='is']")
    SMART_PL_VALUE_FILD = (By.CSS_SELECTOR, "input[name='value[]']")
    SMART_PL_ADD_RULE = (By.CSS_SELECTOR, "button.btn-add-rule")
    SMART_PL_ADD_GROUP = (By.CSS_SELECTOR, "button.btn-add-group")
    SMART_PL_SAVE_BTN = (By.XPATH, "//footer/button[@type='submit']")
    PLAY_LIST_NEW_LIST11 = (By.XPATH, "//a[@class='active' and (text()='New_list11')]")

    def move_mouse_to_create_playlist(self):
        smart_pl = self.find_element(*self.CREATE_PLAYLIST_BTN)
        self.actions.move_to_element(smart_pl).click().perform()

    def click_create_new_playlist(self):
        self.click(*self.NEW_PLAYLIST_BTN)

    def click_smart_playlist_menu(self):
        self.click(*self.SMART_PLAYLIST_MENU)

    def enter_name_smpl(self, text):
        self.input_text(text, *self.SMART_PL_NAME_FIL)

    def select_rul_title(self):
        self.click(*self.SMART_PL_MODEL_FILD)

    def select_rul_operator(self):
        self.click(*self.SMART_PL_OPERATOR_FILD)

    def enter_rul_value(self, text):
        self.input_text(text, *self.SMART_PL_VALUE_FILD)

    def click_save_pl_btn(self):
        self.click(*self.SMART_PL_SAVE_BTN)

    def verify_playlist_create(self, text):
        self.verify_text(text, *self.PLAY_LIST_NEW_LIST11)



