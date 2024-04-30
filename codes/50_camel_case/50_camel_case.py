def camelcase(s):
    count = 1
    for ch in s:
        if ch.isupper():
            count += 1
    return count


print(camelcase('oneTwoThree'))
