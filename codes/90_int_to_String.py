"""
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
"""


def compute_length(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s1) == len(s2):
        return s1, s2
    return s2


str1 = input("Enter string 1 :\n")
str2 = input("Enter string 1 :\n")
print(compute_length(str1, str2))
