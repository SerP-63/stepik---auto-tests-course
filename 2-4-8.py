from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Ждем число 100 на счетчике
Wait = WebDriverWait(browser, 12)
Wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
# Жмем кнопку
browser.find_element_by_id("book").click()
browser.execute_script("window.scrollBy(0, 100);")

try:
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answ_elem = browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()