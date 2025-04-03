*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
launchBrowserWithoutArguments
    open browser    ${url}  ${browser}
    maximize browser window

launchBrowserWithArguments
    [Arguments]  ${appurl}    ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window

launchBrowserWithArgumentsandReturnValue
    [Arguments]  ${appurl}    ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]  ${title}