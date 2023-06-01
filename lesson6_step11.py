from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    pict = browser.find_element(By.ID, "treasure")
    pic_val = pict.get_attribute('valuex')
    print(pic_val)
    cunt = calc(pic_val)
    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(cunt)
    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    sub_btn = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
