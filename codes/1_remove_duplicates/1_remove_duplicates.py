def remove_duplicates(nums):
    if not nums:
        return 0

    nums.sort()

    slow = 0
    fast = 1

    # Move the fast pointer to find the next non-duplicate element
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    # Resize the list to remove the duplicates
    nums[:] = nums[:slow + 1]

    return nums


nums = [1, 2, 2, 3, 4, 4, 4, 5]
nums = remove_duplicates(nums)
print(nums)