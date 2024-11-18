*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  jon
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Register Should Fail

Register With Valid Username And Too Short Password
    Set Username  jon
    Set Password  abcd123
    Set Password Confirmation  abcd123
    Submit Credentials
    Register Should Fail

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  jon
    Set Password  abcdabcd
    Set Password Confirmation  abcdabcd
    Submit Credentials
    Register Should Fail

Register With Nonmatching Password And Password Confirmation
    Set Username  jon
    Set Password  abcd1234
    Set Password Confirmation  abcd1235
    Submit Credentials
    Register Should Fail

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Register Should Fail

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page