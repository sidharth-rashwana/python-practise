def marsExploration(s):
    expected = 'SOS' * (len(s) // 3)
    print('expected', expected)
    d = zip(expected, s)
    print(list(d))
    return len([a for a, b in zip(expected, s) if a != b])


print(marsExploration('SOSOOSOSOSOSOSSOSOSOSOSOSOS'))
print(marsExploration('SOSSTT'))
print(marsExploration('SOSSTTSRR'))
