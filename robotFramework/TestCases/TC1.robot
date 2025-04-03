*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
LoginTest
    open browser    ${url}     ${browser}
    click link  xpath://a[contains(text(),'Log in')]
    input text  id:Email    babisamineedi123@gmail.com
    input text  id:Password     12345
    click element   xpath://button[contains(text(),'Log in')]
    close browser

LoginTest1
    open browser    ${url}     ${browser}
    loginToApplicaton
    close browser

*** Keywords ***
loginToApplicaton
    click link  xpath://a[contains(text(),'Log in')]
    input text  id:Email    babisamineedi123@gmail.com
    input text  id:Password     12345
    click element   xpath://button[contains(text(),'Log in')]

