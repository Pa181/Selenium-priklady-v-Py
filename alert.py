from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    element_input = browser.find_element_by_css_selector("#answer")
    element_input.send_keys(y)
    button2 = browser.find_element_by_css_selector(".btn-primary")
    button2.click()

    ai = browser.switch_to.alert
    ai.accept()







finally:
    time.sleep(60)
    browser.quit()