"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""


def print_even(n):
    for i in n:
        if i % 2 == 0:
            print(i)


n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print_even(n)
