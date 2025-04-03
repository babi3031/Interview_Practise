*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demowebshop.tricentis.com/register

*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    ${implicittime}=      get selenium implicit wait  #default 0 seconds
    log to console      ${implicittime}
    set selenium implicit wait    10 seconds
    select radio button     Gender  M
    input text      name:FirstName1      Babi
    input text      name:LastName      Samineedi
    input text      name:Email      babisamineedi@gmail.com
    input text      name:Password      babisamineedi
    input text      name:ConfirmPassword      babisamineedi

*** Keywords ***
