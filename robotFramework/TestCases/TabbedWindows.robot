*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
TabbedWindowsTest
    open browser    https://demo.automationtesting.in/Windows.html     chrome
    maximize browser window
    click element   xpath://body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/button[1]
    switch window   title=Selenium
    click element   xpath://span[contains(text(),'Documentation')]
    sleep   5
    #close browser it will close recently open browser
    close all browsers  #closes all browsers which all are opened

*** Keywords ***