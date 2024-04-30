"""
With a given tuple (1,2,3,4,5,6,7,8,9,10),
write a program to print the first half values in one line and the last half values in one line.
"""


def print_tuple(t):
    total = len(t)
    half = int(total / 2)
    print(t[:half])
    print(t[half:])


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print_tuple(t)
