"""
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and
the values are square of keys.
"""


def print_dict(s, e):
    d = {}
    for i in range(s, e + 1):
        d[i] = i ** 2
    return d


s = int(input("Enter start number: \n"))
e = int(input("Enter end number: \n"))
print(print_dict(int(s), int(e)))
