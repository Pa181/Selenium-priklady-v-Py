from selenium import webdriver
import time
import math

try:
    link = "https://www.seznam.cz"
    browser = webdriver.Chrome()
    browser.get(link)

    #def calc(x):
      # return str(math.log(abs(12*math.sin(int(x)))))
    time.sleep(5)
    #Najit selector pro X
    x_element = browser.find_element_by_css_selector("[username]")
    x_element.click()
    x_element.send_keys("daripalo")

    x_element1 = browser.find_element_by_css_selector("")
    x_element1.click()
    x_element1.send_keys("")

   # d_element1 = browser.find_element_by_css_selector("szn-select")
    #d_element1.click()
    #d_element = browser.find_element_by_css_selector("szn-select--button :nth=child(1)")
    #d_element.click()
    #Najit selector pro button "Submit"
    #button2 = browser.find_element_by_css_selector(".btn-default")
    #button2.click()

finally:
    time.sleep(30)
    browser.quit()

