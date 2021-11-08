from selenium import webdriver
import time 

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputName = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    inputName.send_keys("Ksenia")
    inputSurname = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    inputSurname.send_keys("Anikeva")
    inputEmail = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    inputEmail.send_keys("anikievak@ya.ru")
    inputPhone = browser.find_element_by_css_selector('[placeholder="Input your phone:"]')
    inputPhone.send_keys("7910000000")
    inputPhoneAddrss = browser.find_element_by_css_selector('[placeholder="Input your address:"]')
    inputPhoneAddrss.send_keys("Russia, Spb")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()