from typing import List


class Solution:
    def findMedianSortedArrays(
            self,
            nums1: List[int],
            nums2: List[int]) -> float:
        median_list = sorted(nums1 + nums2)
        if len(median_list) % 2 != 0:
            median = median_list[len(median_list) // 2]
        else:
            start = len(median_list) // 2 - 1
            end = len(median_list) // 2 + 1
            median = sum(median_list[start:end]) / 2
        return median


s1 = Solution()
print(s1.findMedianSortedArrays([1, 2], [3, 4]))
