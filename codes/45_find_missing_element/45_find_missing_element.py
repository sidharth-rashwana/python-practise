arr = [3, 7, 1, 2, 8, 4, 5]


def find_missing_numbers(arr):
    max_elem = max(arr)
    maximum = [i for i in range(1, max_elem + 1)]
    a1 = set(arr)
    a2 = set(maximum)
    res = list(a2 - a1)
    return res[0]


print(find_missing_numbers(arr))
