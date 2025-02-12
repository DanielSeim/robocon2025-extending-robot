*** Settings ***
Library            Library.py

*** Test Cases ***
Argument conversion
    Conversion
    ...    42
    ...    ${CURDIR}/tests.robot
    ...    1 minute 7 seconds

Restricted values
    Move    UP
    Move    left
    #Move    BAD
    Turn    LEFT
    Turn    right
    Turn    wrong