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

    #Selecting Dropdown Boxes
    select from list by label   continents  Asia
    select from list by index   continents  5

    #Selecting List Box
    select from list by label   selenium_commands   Switch Commands
    select from list by label   selenium_commands   Subelement Commands
    Sleep   4
    unselect feom list by label   selenium_commands   Switch Commands

    close browser

*** Keywords ***
