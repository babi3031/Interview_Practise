from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    status = (context.driver.
              find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed())
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()

