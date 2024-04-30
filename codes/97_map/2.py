"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""


def sq_even(n):
    n = map(lambda x: x * x, filter(lambda x: x % 2 == 0, n))
    return list(n)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sq_even(n))
