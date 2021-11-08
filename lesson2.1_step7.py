from selenium import webdriver
import time 
import math

def CalculatePredefined(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/get_attribute.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    x_element = browser.find_element_by_id("treasure") #find the x_element
    x = x_element.get_attribute("valuex") #use x_element text for x
    y = CalculatePredefined(x) #set up y variable

    inputResult = browser.find_element_by_id("answer") #locate input field
    inputResult.send_keys(y) #fill in input field
    
    checkbox = browser.find_element_by_id("robotCheckbox") #find checkbox
    checkbox.click() #click checkbox
    radiobutton = browser.find_element_by_id("robotsRule") #find radiobutton
    radiobutton.click() #click radiobutton
    submitButton = browser.find_element_by_tag_name("button") #find submit button
    submitButton.click() #click submit button
    

finally:
    time.sleep(10)
    browser.quit()