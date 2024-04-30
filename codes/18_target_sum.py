# return index of elements whose sum equal to target
def match_target(nums, target):
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums[i + 1:]:
            return [i, nums.index(complement, i + 1)]
    return [0, 0]


print(match_target([3, 2, 4], 6))
print(match_target([3, 3], 6))
print(match_target([2, 7, 11, 15], 9))
