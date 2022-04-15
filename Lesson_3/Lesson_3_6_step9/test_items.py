import time

def test_addToBasketButton_Check(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.implicitly_wait(10)

        browser.get(link)
#        time.sleep(30)
        button = browser.find_elements_by_class_name("btn-add-to-basket")
        assert button, \
            f"Wrong test, there is no button"