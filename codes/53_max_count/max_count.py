def pickingNumbers(a):
    max_count = 0
    lst = []
    for num in a:
        if num not in lst:
            count = a.count(num) + a.count(num + 1)
            lst.append(num)
            if count > max_count:
                max_count = count
    return max_count


a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(pickingNumbers(a))
