*** Settings ***
Suite Setup  log to console     Opening Browser
Suite Teardown  log to console     Closing Browser
Test Setup  log to console      Login to application
Test Teardown  log to console       Logout from application
*** Variables ***

*** Test Cases ***
TC1 Prepaid Recharge
    log to console      This prepaid recharge testcase
TC2 Postpaid Recharge
    log to console      This postpaid recharge testcase
TC3 search
    log to console      This is search testcase
TC4 Advanced search
    log to console      This is Adv search testcase
*** Keywords ***