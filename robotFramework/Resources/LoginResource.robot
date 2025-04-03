*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${loginURL}    https://admin-demo.nopcommerce.com/
${browser}  chrome

*** Keywords ***
Open my Browser
    open browser    ${loginURL}     ${browser}
    maximize browser window

Close Browers
    close all browsers

Open Login Page
    go to ${loginURL}

Input Username
    [Arguments]     ${username}
    input text  id:Email    ${username}

Input Pwd
    [Arguments]     ${password}
    input text  id:Password    ${password}

Click login button
    click element   xpath://button[contains(text(),'Log in')]

click logout button
    click link  Logout

error message should be visible
    page should contain     Login was unsuccessful

dashboard page should be visible
    page should contain     Dashboard
