"""
Tags : #unique-dictionaries-in-list
"""


def pair_of_socks(socks):
    visited = []
    d = {}
    for i in socks:
        if i not in visited:
            visited.append(i)
            count = socks.count(i)
            total_count = count // 2
            if i not in d:
                if total_count != 0:
                    d[i] = total_count
    print('Pair of socks : ', d)
    return sum(d.values())


print('Total Pairs : ', pair_of_socks([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print('Total Pairs : ', pair_of_socks([1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
