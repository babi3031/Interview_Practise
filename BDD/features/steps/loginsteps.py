from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,
                                "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(user)
    context.driver.find_element(By.XPATH,
                                "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    except:
        context.driver.close()
        assert False,'Test Failed'
    if text == "Dashboard":
        context.driver.close()
        assert True,'Test Passed'