from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")
browser.get('https://techstepacademy.com/training-ground')

# print("I have arrived")
# WebDriverWait(browser,10).until(alert_is_present())
# print("An alert appeared")

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)
my_select.select_by_visible_text('Beets')
