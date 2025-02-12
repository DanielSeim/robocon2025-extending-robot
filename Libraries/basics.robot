*** Settings ***
Library    basics.py

*** Test Cases ***
Simple Keyword
    Simple Keyword

Arguments
    One Argument    Robot
    Default Values    Robot    
    Default Values    Robot    Hi

Status
    Should Be Positive    1
    Should Be Positive    1.3
    Should Be Positive    -1

Logging
    Log Using Print
    Log Using API