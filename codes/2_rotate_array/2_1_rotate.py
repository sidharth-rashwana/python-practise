def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        val = nums.pop()
        nums.insert(0, val)
    print(nums)


print(rotate([1, 2, 3], 2))
