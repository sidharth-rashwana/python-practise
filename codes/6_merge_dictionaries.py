"""
Given two dictionaries dict1 and dict2, merge them to create a new dictionary with all the key-value pairs from both dictionaries.
"""

dict1 = {"a": 1, "b": 2, "c": 3}

dict2 = {"c": 4, "d": 5, "e": 6}

dict2.update(dict1)

print(dict2)
