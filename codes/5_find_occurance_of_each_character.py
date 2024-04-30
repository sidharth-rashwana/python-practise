"""
Create a Python program that counts the occurrences of each character in a given string and stores the results in a dictionary.
"""
input_string = "abracadabra"

d = {}

for ch in input_string:
    if ch not in d:
        occurance = input_string.count(ch)
        d[ch] = occurance
print(d)
