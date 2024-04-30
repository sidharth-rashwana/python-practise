def containsDuplicate(nums):
    d = {}
    for k in nums:
        if k not in d.keys():
            d[k] = 1
        else:
            return 'Contain Duplicates'
    return 'Do not Contain Duplicates'


print(containsDuplicate([1, 2, 3, 1]))  # Contains duplicate
print(containsDuplicate([1, 2, 3]))  # Do not contains duplicate
