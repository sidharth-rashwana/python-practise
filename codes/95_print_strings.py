"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""


def print_string(n):
    if n in ["yes", "YES"]:
        print("Yes")
    else:
        print("No")


print_string("yes")
