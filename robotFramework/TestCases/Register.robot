*** Settings ***
Library  SeleniumLibrary
Variables  ..//PageObjects//Locators.py

*** Variables ***
${Browser}  chrome
${SiteUrl}  https://demo.guru99.com/test/newtours/
${user}     davidjohn
${pwd}  davidjohn@

*** Test Cases ***
RegisterTest
    open browser     ${SiteUrl}      ${Browser}
    Maximize Browser Window
    click link  ${link_Reg}
    Input Text  ${txt_first_name}    David
    Input Text  ${txt_last_name}    John
    Input Text  ${txt_phone}    1234567890
    Input Text  ${txt_email}    davidjohn@gmail.com
    Input Text  ${txt_address}    canada
    Input Text  ${txt_city}    Toronto
    Input Text  ${txt_state}    Brampton
    Input Text  ${txt_postalCode}    123456
    Input Text  ${txt_username}    ${user}
    Input Text  ${txt_password}    ${pwd}
    Input Text  ${txt_confirmPassword}    ${pwd}
    click button    ${btn_signIn}
    sleep   5
    capture page screenshot     register.png
    page should contain    Thank you for registering.
    close all browsers

*** Keywords ***

