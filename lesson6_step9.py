from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)

    input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_text.send_keys(y)

    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    sub_btn = browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
