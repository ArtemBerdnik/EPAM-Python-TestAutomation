*** Settings ***
Documentation     A test cases for HW14
Library     SeleniumLibrary
Library     ../libraries/pageobjects/MonitorsPage.py
Library     ../libraries/pageobjects/CartPage.py
Variables   ../libraries/variables.py

*** Variables ***
${URL}  https://www.demoblaze.com/
${USERNAME}     ArtemB
${PASSWORD}     ArtemB

*** Test Cases ***
hw_part_1
    Open Browser    ${URL}   chrome
    Login with valid credentials    ${USERNAME}     ${PASSWORD}
    Element Should Be Visible   ${LOGOUT_BUTTON}
    Element Text Should Be  ${WELCOME_MESSAGE_TEST}  Welcome ${USERNAME}

hw_part_2
    Open Browser    ${URL}   chrome
    Login with valid credentials    ${USERNAME}     ${PASSWORD}
    Click Element   ${MONITORS_BUTTON}
    BuiltIn.Sleep   2
    ${MOST_EXPENCIVE_MONITOR}=     MonitorsPage.Find The Most Expensive Monitor
    Click Element   ${MOST_EXPENCIVE_MONITOR}[0]
    Wait Until Element Is Visible   ${PRODUCT_NAME_ON_PRODUCT_PAGE}
    Title should be correct in product page     ${MOST_EXPENCIVE_MONITOR}[1]
    Price should be correct in product page     $${MOST_EXPENCIVE_MONITOR}[2] *includes tax
    Click Element    ${ADD_TO_CARD_BUTTON}
    Alert Should Be Present     Product added.
    Click Element    ${CART_BUTTON}
    CartPage.Wait Until Table Is Loaded
    Title should be correct in cart     ${MOST_EXPENCIVE_MONITOR}[1]
    Price should be correct in cart     ${MOST_EXPENCIVE_MONITOR}[2]


*** Keywords ***
Login with valid credentials
    [Documentation]     uses valid credentials to log in
    [Arguments]     ${valid_username}     ${valid_password}
    Click Element   ${LOGIN_BUTTON}
    Wait Until Element Is Visible   ${LOGIN_POPUP}
    Element Should Be Visible   ${LOGIN_POPUP}
    BuiltIn.Sleep   1
    Input Text  ${USERNAME_INPUT_FIELD}    ${valid_username}
    Input Password  ${PASSWORD_INPUT_FIELD}    ${valid_password}
    Click Element   ${LOGIN_BUTTON_IN_LOGIN_POPUP}
    Wait Until Element Is Visible   ${LOGOUT_BUTTON}


Title should be correct in product page
    [Documentation]     verifies that in the product page the name of a product is correct
    [Arguments]     ${expected_name}
    [Tags]  custom_screenshot
    ${ACTUAL_NAME}=   Get Text    ${PRODUCT_NAME_ON_PRODUCT_PAGE}
    Should Be Equal     ${expected_name}    ${ACTUAL_NAME}


Price should be correct in product page
    [Documentation]     verifies that in the product price the name of a product is correct
    [Arguments]     ${expected_price}
    [Tags]  custom_screenshot
    ${ACTUAL_PRICE}=   Get Text    ${PRODUCT_PRICE_ON_PRODUCT_PAGE}
    Should Be Equal     ${expected_price}    ${ACTUAL_PRICE}


Title should be correct in cart
    [Documentation]     verifies that in the cart the name of a product is correct
    [Arguments]     ${expected_name}
    [Tags]  custom_screenshot
    ${ACTUAL_NAME_IN_CART}=   Get Text    ${PRODUCT_NAME_IN_CART}
    Should Be Equal     ${expected_name}    ${ACTUAL_NAME_IN_CART}

Price should be correct in cart
    [Documentation]     verifies that in the cart the price of a product is correct
    [Arguments]     ${expected_price}
    [Tags]  custom_screenshot
    ${ACTUAL_PRICE_IN_CART}=   Get Text    ${PRODUCT_PRICE_IN_CART}
    Should Be Equal     ${expected_price}    ${ACTUAL_PRICE_IN_CART}
