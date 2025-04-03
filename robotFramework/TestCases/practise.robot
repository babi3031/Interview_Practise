*** Settings ***
Library    C:\\Babi\\robotFramework\\PageObjects\\MyLibrary.py

*** Test Cases ***
Add Numbers
    ${status}    Run Keyword And Return Status    Click Button    non_existing_button
    Run Keyword If    '${status}'=='False'    Log    Button was not found

*** Test Cases ***
Login With Multiple Users
    [Arguments]    ${username}    ${password}
    Login To Application    ${username}    ${password}

*** Variables ***
@{users}    user1    pass1    user2    pass2

*** Test Cases ***
Test Login
    : FOR    ${user}    IN    @{users}
    \    Login With Multiple Users    ${user}[0]    ${user}[1]


