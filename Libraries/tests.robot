*** Settings ***
Library            Library.py    state=ORIGINAL

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

Restricted values using ENUM
    Turn    LEFT
    Turn    right
    #Turn    wrong


Custom converts
    Birthday    22.01.1991


Library state 1
    Set State    NEW
    Set State    NEWER


Library state 2
    Set State    NEWEST


Custom keyword name
    🤖


Embedded arguments
    This is a "good" example
    This is a "bad" example
    This is a "ugly" example


Mixed arguments
    Number of horses is    6
    Number of dogs is     2


Skipping
    Skip me


Continuing on failure
    Continuable failure    first
    Continuable failure    second
    Continuable failure    third


HTML error messages
    HTML error
