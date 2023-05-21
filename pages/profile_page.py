from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProfilePage(Page):

    CURRENT_PASSWORD = (By.XPATH, "//input[@name='current_password']")
    NAME = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "input[name='email']")
    NEW_PASSWORD = (By.CSS_SELECTOR, "input[name='new_password']")
    SAVE_BTN = (By.XPATH, "//button[text()='Save']")
    COLOR_VIOLET = (By.XPATH, "//div[text()='Violet']")
    COLOR_ROCKY = (By.XPATH, "//div[text()='Rocky Mountain High']")
    SELECT_FRAME = (By.CSS_SELECTOR, "div.theme.selected")
    CHECKBOX_CONFIRM = (By.CSS_SELECTOR, "input[name='confirm_closing']")

    def click_color_violet(self):
        self.click(*self.COLOR_VIOLET)

    def click_color_rocky(self):
        self.click(*self.COLOR_ROCKY)

    def click_checkbox_confirm(self):
        self.click(*self.CHECKBOX_CONFIRM)

    def wait_for_element_activ(self):
        self.wait_for_element_click(*self.SELECT_FRAME)