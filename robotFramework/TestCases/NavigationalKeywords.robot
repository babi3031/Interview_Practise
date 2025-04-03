*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
NavigationTest
    open browser    https://www.google.com/     chrome
    maximize browser window
    ${loc}=     get location
    log to console      ${loc}

    go to   https://www.bing.com/
    ${loc}=     get location
    log to console      ${loc}
    sleep   4
    go back
    ${loc}=     get location
    log to console      ${loc}
    sleep   3
    close browser
*** Keywords ***