*** Settings ***
Library    Dynamic.py


*** Test Cases ***
Keyword name
    Dynamic keyword

Arguments
    Arguments    hello
    Arguments    arg1    arg2
    Arguments    arg1    second=arg2