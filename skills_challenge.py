from selenium import webdriver
browser = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")
browser.get('https://techstepacademy.com/trial-of-the-stones')

# Riddle of Stones
stone_input = browser.find_element_by_id('r1Input')
stone_answer_butn = browser.find_element_by_css_selector("button#r1Btn")
stone_result = browser.find_element_by_css_selector("div#passwordBanner > h4")

# Riddle of Secrets
secrets_input = browser.find_element_by_css_selector("input#r2Input")
secrets_answer_butn = browser.find_element_by_css_selector("button#r2Butn")

# Two Merchants
# Simple Approach
richest_merchant_name = browser.find_element_by_xpath(
    "//p[text()='3000']/../span"
)
merchant_input = browser.find_element_by_id('r3Input')
merchant_answer_butn = browser.find_element_by_css_selector(
    "button#r3Butn"
)
# Check Result
check_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)
complete_msg = browser.find_element_by_css_selector("div#trialCompleteBanner > h4")

## Testing
stone_input.send_keys('rock')
stone_answer_butn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_butn.click()

merchant_input.send_keys(richest_merchant_name.text)
merchant_answer_butn.click()

check_butn.click()
assert complete_msg.text == 'Trial Complete'