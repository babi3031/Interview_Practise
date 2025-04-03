*** Settings ***
Library  SeleniumLibrary
Resource  C://Babi//robotFramework//Resources//LoginResource.robot
Suite Setup  Open my Browser
Suite Teardown  Close Browers
Test Template  Invalid Login

*** Variables ***


*** Test Cases ***               username                 password
Tc1_Right_user_empty_pwd        admin@yourstore.com        ${empty}
Tc2_Right_user_wrong_pwd        admin@yourstore.com        xyz
Tc3_Wrong_user_right_pwd        admi@yourstore.com         admin
Tc4_Wrong_user_empty_pwd        adn@yourstore.com          ${empty}
Tc5_Wrong_user_wrong_pwd        amin@yourstore.com         xyz


*** Keywords ***
Invalid Login
    [Arguments]  ${username}    ${password}
    Input Username  ${username}
    Input Pwd  ${password}
    Click login button
    error message should be visible