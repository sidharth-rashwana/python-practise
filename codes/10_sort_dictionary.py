"""
Write a Python function to find the top N (e.g., 5) items with the highest values in a given dictionary.
"""
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}

# sort by values
sorted_values = dict(sorted(scores.items(), key=lambda item: item[1]))
# sort by keys
sorted_keys = dict(sorted(scores.items(), key=lambda item: item[0]))

print('sort by key name : ', sorted_keys, '\nsort by value : ', sorted_values)

# reverse a dictionary
rev_value = dict(reversed(list(sorted_values.items())))

count = int(input('\nHow many top N items : \n'))

top_candidate = {}

current = 0

for element in rev_value:
    if current == count:
        break
    if current != count:
        top_candidate[element] = rev_value[element]
        current += 1

print(f'Top {count} candidate(s): ', top_candidate)
