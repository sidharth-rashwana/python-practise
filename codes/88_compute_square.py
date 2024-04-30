"""
Write a method which can calculate square value of number
"""


class Square:
    def __init__(self):
        self.sq = 0

    def square(self, n):
        self.sq = n * n

    def __str__(self):
        return f"square: {self.sq}"


o = Square()
result = o.square(10)
print(o)
