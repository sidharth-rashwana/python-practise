"""
In simpler terms, the program counts how many numbers between the largest number in `a` and the smallest number in `b` (inclusive)
are divisible by all numbers in a and also divide all numbers in b.
"""


def solve(a, b):
    max_a = max(a)
    min_b = min(b)
    cnt = 0
    for i in range(max_a, min_b + 1):
        if all(i % x == 0 for x in a) and all(y % i == 0 for y in b):
            # 4 and 12 are divisible by all members in a ; and also 4 and 12
            # divides all members in b
            print(i)
            cnt += 1
    return cnt


a = [2, 4]
b = [24, 36]
print(solve(a, b))
