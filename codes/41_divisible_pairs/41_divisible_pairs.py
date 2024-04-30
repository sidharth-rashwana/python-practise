def divisibleSumPairs(n, k, ar):
    final = []
    for i in range(len(ar) - 1):
        for j in range(1, len(ar)):
            if ((ar[i] + ar[j]) % k) == 0 and i < j:
                d = {}
                d = {i, j}
                final.append(d)
    return len(final)


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(n, k, ar))
