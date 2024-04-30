"""
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

import re


def check_password(password):
    if len(password) < 6:
        return 'length is less than 6.'
    if not re.search('[a-z]', password):
        return 'does not contain letter among [a-z]'
    if not re.search('[0-9]', password):
        return 'does not contain digit among [0-9]'
    if not re.search('[A-Z]', password):
        return 'does not contain digit among [A-Z]'
    if not re.search('[$#@]', password):
        return 'does not contain digit among [$#@]'
    return 'valid'


username = input("Enter username: ")
password = input("Enter password: ")

print(check_password(password))
