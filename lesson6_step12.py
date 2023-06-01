from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    y = calc(num1,num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()