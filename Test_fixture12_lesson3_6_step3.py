import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_alien_message(browser, link):
        answer = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(link)
        input = browser.find_element_by_class_name("ember-text-area")
        input.send_keys(answer)
        button = browser.find_element_by_class_name("submit-submission")
        button.click()
        feedback = browser.find_element_by_class_name("smart-hints__hint").text
        assert feedback == "Correct!", \
            f"Wrong test, got {feedback}instead of 'Correct!'"
        