from selenium import webdriver
import time 
import math

def CalculatePredefined(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    wantButton = browser.find_element_by_tag_name("button") #find submit button
    wantButton.click() #click submit button

    confirmModal = browser.switch_to.alert #select comfirm modal
    confirmModal.accept() #accept confirm modal

    time.sleep(1) #wait for the page

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = CalculatePredefined(x)

    inputField = browser.find_element_by_id("answer")
    inputField.send_keys(y)

    submitButton = browser.find_element_by_tag_name("button") #find submit button
    submitButton.click() #click submit button    

finally:
    time.sleep(10)
    browser.quit()