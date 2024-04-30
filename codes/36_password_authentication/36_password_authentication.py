def calculate_hash(s, P, M):
    n = len(s)
    h = 0
    for i, ch in enumerate(s):
        h += ord(ch) * (P**(n - 1 - i))
    return h % M


def authEvents(events):
    d = {}
    for event in events:
        if event[0] == 'setPassword':
            s = event[1]
            P = 131  # You can adjust the value of P as needed
            M = 10**9 + 7
            hash_value = calculate_hash(s, P, M)
            d[event[0]] = hash_value

    return d


result = authEvents([['setPassword', 'cAr1']])
print(result)
