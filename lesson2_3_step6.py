from selenium import webdriver
import time 
import math

def CalculatePredefined(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    wantButton = browser.find_element_by_tag_name("button") #find submit button
    wantButton.click() #click submit button    
    new_tab = browser.window_handles[1] #give the name to new tab
    browser.switch_to.window(new_tab) #select the new tab

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