*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
MouseActionsTest
    open browser    https://swisnl.github.io/jquery-contextMenu/demo.html     chrome
    maximize browser window
    sleep   5
    input text  name:username   babi
    input text  name:password   babi
    capture page screenshot     page1.png
    sleep   5
    capture element screenshot      xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]   element1.png
    close browser
*** Keywords ***