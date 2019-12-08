from selenium import webdriver
browser1 = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")
browser2 = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")

browser1.get('https://techstepacademy.com/training-ground')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')

browser2.get('https://google.com')

handles = browser1.window_handles
browser1.switch_to.window(handles[1])
