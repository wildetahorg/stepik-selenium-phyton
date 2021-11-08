from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html" #set up variable for link
browser = webdriver.Chrome() #set up variable for browser

try: 
    browser.get(link) #open link

    firstNameInput = browser.find_element_by_name("firstname") #find the element
    firstNameInput.send_keys("John") #fill in the field
    lastNameInput = browser.find_element_by_name("lastname") #find the element 
    lastNameInput.send_keys("Doe") #fill in the field
    emailInput = browser.find_element_by_name("email") 
    emailInput.send_keys("test@email.com")

    addFileInput = browser.find_element_by_id("file")    #find the element for adding file
    current_dir = os.path.abspath(os.path.dirname(__file__)) #get the path to the running file
    file_path = os.path.join(current_dir, 'random_file.txt') #find the random_file.txt in the dir
    
    addFileInput.send_keys(file_path) #upload file

    submitButton = browser.find_element_by_tag_name("button") #find submit button
    submitButton.click() #click submit button

finally:
    time.sleep(10)
    browser.quit()