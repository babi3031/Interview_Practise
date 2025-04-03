*** Settings ***
Library  SeleniumLibrary
Resource  ..Resources//Resources.robot
*** Variables ***
${url}  https://demo.guru99.com/test/newtours/
${browser}  chrome

*** Test Cases ***
Tc1launchBrowserWithoutArguments
    launchBrowserWithoutArguments
    input text  name:userName   mercury
    input text  name:password   mercury
    close browser

Tc2launchBrowserWithArguments
    launchBrowserWithArguments  ${url}  ${browser}
    input text  name:userName   mercury
    input text  name:password   mercury
    close browser

Tc3launchBrowserWithArgumentsandReturnValue
    ${Apptitle}=   launchBrowserWithArgumentsandReturnValue  ${url}  ${browser}
    log to console  ${Apptitle}
    log     ${Apptitle}
    input text  name:userName   mercury
    input text  name:password   mercury
    close browser

