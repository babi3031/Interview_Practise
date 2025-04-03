*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
LoginTest
    open browser    https://demo.nopcommerce.com/     chrome
    maximize browser window

    open browser    https://demowebshop.tricentis.com/register     chrome
    maximize browser window
    #close browser it will close recently open browser
    close all browsers  #closes all browsers which all are opened

*** Keywords ***


