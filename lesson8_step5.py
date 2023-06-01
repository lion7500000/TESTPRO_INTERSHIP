from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(y)

    check_box = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    check_box.click()

    sub_btn = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", sub_btn)
    sub_btn.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) # заставить браузер дополнительно проскроллить нужный элемент
    # // javascript
    # button = document.getElementsByTagName("button")[0];
    # button.scrollIntoView(true);


finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()