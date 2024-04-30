"""
Write a Python function that returns the intersection of two dictionaries, containing only the key-value pairs that exist in both dictionaries.
"""

dict1 = {"a": 1, "b": 2, "c": 3}

dict2 = {"c": 3, "d": 4, "e": 5}

intersection = {k: v for k, v in dict1.items() if k in dict2 and dict2[k] == v}
print(intersection)
