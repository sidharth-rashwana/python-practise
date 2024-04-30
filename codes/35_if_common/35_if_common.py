def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return 'YES'
    return 'NO'


# Call the function with strings, not lists
print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))
