*** Settings ***
Library  SeleniumLibrary
Resource   C:\Babi\robotFramework\Resources\LoginKeywords.robot
Variables  ..//PageObjects//Locators.py

*** Variables ***
${Browser}  chrome
${SiteUrl}  https://demo.guru99.com/test/newtours/
${user}     tutorial
${pwd}  tutorial

*** Test Cases ***
LoginTest
#    Open my Browser     ${SiteUrl}      ${Browser}
#    Enter UserName      ${user}
#    Enter Password      ${pwd}
#    Click SignIn
#    Verify Successful Login
#    Close My Browsers
    open Browser     ${SiteUrl}      ${Browser}
    Maximize Browser Window
    Input Text  ${txt_loginUserName}    ${user}
    Input Text  ${txt_loginPassword}    ${pwd}
    click button    ${btn_signIn}
    title should be  Login: Mercury Tours
    close all browsers

*** Keywords ***

