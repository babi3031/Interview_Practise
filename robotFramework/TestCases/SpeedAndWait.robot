*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demowebshop.tricentis.com/register

*** Test Cases ***
TestingInputBox
    ${speed}=      get selenium speed
    #log     ${speed}
    log to console      time${speed}
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed      1seconds
    select radio button     Gender  M
    input text      name:FirstName      Babi
    input text      name:LastName      Samineedi
    input text      name:Email      babisamineedi@gmail.com
    input text      name:Password      babisamineedi
    input text      name:ConfirmPassword      babisamineedi
    #capture page screenshot      speedandsleep.png
    #Sleep   5
    close browser

*** Keywords ***
