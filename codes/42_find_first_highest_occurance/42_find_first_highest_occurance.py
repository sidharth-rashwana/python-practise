# arr = [3,1,2,2,1]
arr = [1, 4, 4, 4, 5, 3]
high = 0
arr.sort()
pair = {}
total_elem = []
for i in arr:
    if i not in total_elem:
        total_elem.append(i)
        c = arr.count(i)
        if c > high:
            high = c
            pair = {i: high}
print(list(pair.keys())[0])
