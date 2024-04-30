"""
Write a function that removes all occurrences of a specific value from a dictionary.
"""

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}

value_to_remove = 1

items = {k: v for k, v in my_dict.items() if v != value_to_remove}

print(items)
