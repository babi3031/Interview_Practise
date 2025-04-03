*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.practiceselenium.com/practice-form.html

*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed      2seconds

    #Selecting Radio Buttons
    select radio button     sex     Female
    select radio button     exp     5

    #Selecting Check Box
    select checkbox     BlackTea
    select checkbox     RedTea
    unselect checkbox       BlackTea

    close browser

*** Keywords ***
