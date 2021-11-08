from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/selects1.html" #set up variable for link
link = "http://suninjuly.github.io/selects2.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    x_element = browser.find_element_by_id("num1") #find the x_element
    x = x_element.text #use x_element text for x
    y_element = browser.find_element_by_id("num2") #find the y_element
    y = y_element.text #use y_element text for y

    z = str(int(x)+int(y)) #set up z variable

    # dropdown = Select(browser.find_element_by_id("dropdown"))
    # dropdown.select_by_value(z) #select value=z

    dropdown = browser.find_element_by_id("dropdown") #find dropdown
    dropdown.click() #click dropdown
    dropdown.send_keys(z) #select value=z

    submitButton = browser.find_element_by_tag_name("button") #find submit button
    submitButton.click() #click submit button
    

finally:
    time.sleep(10)
    browser.quit()