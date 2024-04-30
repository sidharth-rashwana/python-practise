def singleNumber(nums):
    visited = []
    for i in nums:
        if i not in visited:
            visited.append(i)
            total = nums.count(i)
            if total == 1:
                return i


print(singleNumber([1, 1, 2, 3, 3]))
