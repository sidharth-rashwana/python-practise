nums = [0, 1, 0, 3, 12]

for i in range(1, len(nums)):
    if nums[i] == 0:
        nums.remove(nums[i])
        nums.append(0)
print(nums)
