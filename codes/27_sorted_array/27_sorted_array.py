from typing import List
'''
binary search approach to find the single element in a sorted array that appears only once in O(log n) time and
O(1) space complexity.
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check if the unique element is on the left or right side of mid
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


s1 = Solution()
s1.singleNonDuplicate([1, 1, 2, 2, 4, 3, 3])
