def divisibleSumPairs(n, k, ar):
    lst = []
    for i in range(0, len(ar) - 1):
        for j in range(1, len(ar)):
            if ((ar[i] + ar[j]) % k) == 0 and i < j:
                t = (ar[i], ar[j],)
                lst.append(t)
    return len(lst)


print(divisibleSumPairs(3, 5, [1, 2, 3, 4, 5, 6]))
