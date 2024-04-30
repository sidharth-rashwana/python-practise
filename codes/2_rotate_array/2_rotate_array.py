def rotate_array(nums, k):
    k %= len(nums)  # Ensure rotation is within the array length
    print(k)
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)


rotate_array([1, 2, 3, 4], 3)
