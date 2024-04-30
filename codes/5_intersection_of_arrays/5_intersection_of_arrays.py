def intersect(lst1, lst2):
    x = set(lst1)
    y = set(lst2)
    c = x.intersection(y)
    print(c)


print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
