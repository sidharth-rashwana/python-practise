"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def count_letters_digits(n):
    print(n, dir(n))
    alpha = 0
    num = 0
    for i in n:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            num += 1
    return f"LETTERS {alpha}", f"DIGITS {num}"


n = "hello world! 123"
digits, numbers = count_letters_digits(n)
print(digits, numbers)
