from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

from features.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://bbb.testpro.io/'
        self.bs_user = 'andrewkoss08@gmail.com11'
        self.bs_pw = 'Andrii1!'
        self.wait = WebDriverWait(self.driver,15)
        self.actions = ActionChains(self.driver)


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def input_text_enter(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text, Keys.ENTER)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_click(self,*locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self,*locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self,*locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    # def hover_mouse_to(self, *locator):
    #     sale_button = self.find_element(locator)
    #     self.actions.move_to_element(sale_button).click().perform()

    def open_page(self, url=''):
        #logger.info(f'Opening page {self.base_url + url}')
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        print(actual_text)
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_found_text(self, search_word, *locator):
        actual_word = self.driver.find_element(*locator).text
        print(actual_word)
        assert search_word in actual_word, f'Expected text {search_word}, but got {actual_word}'

    def verify_len_items(self, expected_items, *locator):
        actual_items = len(self.driver.find_elements(*locator))
        assert int(expected_items) == actual_items, f'Expected text {expected_items}, but got {actual_items}'