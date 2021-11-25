import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def CalculatePredefined(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()#browser should wait every element 5s checking it appearing every 500ms

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    booking = browser.find_element_by_id("book")
    booking.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = CalculatePredefined(x)

    inputField = browser.find_element_by_id("answer")
    inputField.send_keys(y)

    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
