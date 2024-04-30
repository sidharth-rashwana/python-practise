def matchingStrings(strings, queries):
    arr = []
    for q in queries:
        c = strings.count(q)
        arr.append(c)
    return arr


print(matchingStrings(['ab', 'ab', 'abc'], ['abc', 'ab', 'bc']))
