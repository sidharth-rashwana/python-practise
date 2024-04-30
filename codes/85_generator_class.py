"""
Define a class with a generator which can iterate
the numbers, which are divisible by 7, between
a given range 0 and n.
"""


class gen_class:
    def my_gen(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i


gen = gen_class()
elem = gen.my_gen(10)

for i in elem:
    print(i)
