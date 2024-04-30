"""
Write a function that takes a list of words and returns a dictionary where the keys are the words,
and the values are the lengths of the corresponding words.
"""

word_list = ["apple", "banana", "grape", "orange", "watermelon"]

d = {}

for word in word_list:
    d[word] = len(word)

print(d)
