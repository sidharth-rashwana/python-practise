"""
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
"""


def print_tuple(s, e):
    lst = []
    for i in range(s, e + 1):
        lst.append(i * i)
    return tuple(lst)


s = int(input("Enter start : \n"))
e = int(input("Enter end : \n"))
print(print_tuple(s, e))
