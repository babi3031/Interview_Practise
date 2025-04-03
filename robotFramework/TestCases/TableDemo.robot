*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TableValidationsTest
    open browser    https://testautomationpractice/blogspot.com/




GetAllLinksTest
    Open Browser    https://demo.guru99.com/test/newtours/      chrome
    Maximize Browser Window
    ${AllLinksCount}=      Get Element Count   xpath=//a
    Log To Console  Total number of links: ${AllLinksCount}

    FOR    ${i}    IN RANGE    1    ${AllLinksCount + 1}
        ${linkText}=    Get Text    xpath=(//a)[${i}]
        Log To Console    Link ${i}: ${linkText}
    END
    Close All Browsers
