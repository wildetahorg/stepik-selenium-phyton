from selenium import webdriver
import time 
import math

def CalculatePredefined(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    x_element = browser.find_element_by_id("input_value") #find the x_element
    x = x_element.text #use x_element text for x

    y = CalculatePredefined(x) #set up y variable

    inputResultField = browser.find_element_by_id("answer") #locate input field
    inputResultField.send_keys(y) #fill in input field
    
    checkbox = browser.find_element_by_id("robotCheckbox") #find checkbox
    checkbox.click() #click checkbox

    submitButton = browser.find_element_by_tag_name("button") #find submit button
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton) #scroll page to the button
    
    radiobutton = browser.find_element_by_id("robotsRule") #find radiobutton
    radiobutton.click() #click radiobutton
    
    submitButton.click() #click submit button

finally:
    time.sleep(10)
    browser.quit()