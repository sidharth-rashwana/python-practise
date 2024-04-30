"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def div_by_7(start, end):
    numbers = []
    for n in range(start, end + 1):
        if n % 7 == 0 and n % 5 != 0:
            numbers.append(n)
    return numbers, len(numbers)


n, t = div_by_7(2000, 3200)
print('numbers: ', n, 'total:', t)
