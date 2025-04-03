*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
MultipleBrowsersTest
    open browser    https://demo.automationtesting.in/Windows.html     chrome
    maximize browser window
    sleep   4
    open browser    https://www.bing.com/       chrome
    maximize browser window
    switch browser  1
    ${title}=   get title
    log to console      ${title}
    click element   xpath://body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/button[1]

    switch browser  2
    ${title}=   get title
    log to console      ${title}
    sleep   5
    #close browser it will close recently open browser
    close all browsers  #closes all browsers which all are opened

*** Keywords ***