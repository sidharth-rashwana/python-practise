"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def check_upper_lower(str):
    upper, lower = 0, 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower


str = "Hello world!"
print(check_upper_lower(str))
