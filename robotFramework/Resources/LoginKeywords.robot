*** Settings ***
Library  SeleniumLibrary
Variables  ..//PageObjects//Locators.py

*** Variables ***

*** Test Cases ***

*** Keywords ***
Open my Browser
    [Arguments]  ${SiteUrl}  ${Browser}
    open Browser     ${SiteUrl}      ${Browser}
    Maximize Browser Window

Enter UserName
    [Arguments]  ${username}
    Input Text  ${txt_loginUserName}    ${username}

Enter Password
    [Arguments]  ${password}
    Input Text  ${txt_loginPassword}    ${password}

Click SignIn
    click button    ${btn_signIn}

Verify Successful Login
    title should be  Login: Mercury Tours

Close My Browsers
    close all browsers