N = int(input('Enter N'))
lst = []
for i in range(N):
    e = int(input('Enter %s: ' % i))
    lst.append(e)

first = max(lst)
index_first = lst.index(first)
d1 = {index_first: first}
total = 0
d2 = {}
for i in range(len(lst)):
    if lst[i] > total and lst[i] < first:
        total = lst[i]
        index = lst.index(total)
        d2 = {index: total}
print(d1, d2)
