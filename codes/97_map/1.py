"""
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq = list(map(lambda x: x * x, l))
print(sq)
