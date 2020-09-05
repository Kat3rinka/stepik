from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button01 = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button02 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
    button02.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", button02)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button.click()

finally:
    time.sleep(10)
    browser.quit()
