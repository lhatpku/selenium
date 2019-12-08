from selenium import webdriver
browser = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")
browser.get('https://techstepacademy.com/training-ground')

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

# Assign Elements
input2_elem = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)

# Manipulate Elements
input2_elem.send_keys("Test test")
butn4_elem.click()



