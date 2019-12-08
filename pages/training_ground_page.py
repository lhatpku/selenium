from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage
from locator import Locator

class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button1(self):
        locator = Locator(by=By.ID,value='b1')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    
# Our Test
from selenium import webdriver
browser = webdriver.Chrome("/Users/haolu/Documents/shared/chromedriver")

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1','Unexpected button1 text'
trng_page.button1.click()
browser.quit()


# trng_page.type_into_input('it worked')
# txt_from_input = trng_page.get_input_text()
# trng_page.click_button_1()
# assert txt_from_input == 'it worked'
