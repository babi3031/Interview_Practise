*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demowebshop.tricentis.com/register

*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    ${time}=      get selenium timeout  #default 5 seconds
    log to console      ${time}
    set selenium timeout    10 seconds
    wait until page contains    Register
    select radio button     Gender  M
    input text      name:FirstName      Babi
    input text      name:LastName      Samineedi
    input text      name:Email      babisamineedi@gmail.com
    input text      name:Password      babisamineedi
    input text      name:ConfirmPassword      babisamineedi

*** Keywords ***
