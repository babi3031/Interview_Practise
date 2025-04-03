*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/
${url1}  https://www.tutorialspoint.com/

*** Test Cases ***
TestingInputBox
    [Documentation]     My first testcase in pycharm
    open browser    ${url}  ${browser}
    maximize browser window
    title should be     nopCommerce demo store
    click link  xpath://a[contains(text(),'Log in')]
    ${"email_txt"}  set variable    id:Email

    element should be visible   ${"email_txt"}
    element should be enabled   ${"email_txt"}

    input text      ${"email_txt"}  babisamineedi123@gmail.com
    Capture Page Screenshot     page.png
    Sleep   5
    clear element text      ${"email_txt"}
    Sleep   5
    close browser

TestingInputBoxTutorailspoint
    [Documentation]     My fisrst testcase in Tutorialspoint
    open browser    ${url1}     ${browser}
    maximize browser window
    set selenium speed      2seconds
    title should be     Quality Tutorials, Video Courses, and eBooks
    input text      id:mobile-search-strings    angular.js
    click element   xpath://div[@id='mobile-search-string']
    close browser

*** Keywords ***
