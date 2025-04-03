*** Settings ***
Library  SeleniumLibrary
Resource  C://Babi//robotFramework//Resources//LoginResource.robot
Library     DataDriver  C://Babi//robotFramework//TestData//LoginData.csv
Suite Setup  Open my Browser
Suite Teardown  Close Browers
Test Template  Invalid Login

*** Variables ***


*** Test Cases ***
LoginTestDataWithCSV using ${username} and ${password}


*** Keywords ***
Invalid Login
    [Arguments]  ${username}    ${password}
    Input Username  ${username}
    Input Pwd  ${password}
    Click login button
    error message should be visible