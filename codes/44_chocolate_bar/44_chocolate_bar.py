def birthday(s, d, m):
    # contiguous block = m
    # sum of elements in list = d
    pair = []
    len_arr = len(s)
    if len_arr > 2:
        for i in range(len(s) - 2):
            if sum(s[i:i + m]) == d:
                pair.append(s[i:i + m])
    else:
        for i in range(len(s)):
            if sum(s[i:i + m]) == d:
                pair.append(s[i:i + m])
    return len(pair), pair


print(birthday([1, 4], 4, 1))
print(birthday([2, 2, 1, 3, 2], 4, 2))
print(birthday([2, 2, 1, 3, 2], 5, 3))
