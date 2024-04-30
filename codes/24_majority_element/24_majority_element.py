from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        d = {}
        for i in nums:
            value = nums.count(i)
            if value > c:
                c = value
                d[i] = c
        return list(d.keys())[0]


s1 = Solution()
print(s1.majorityElement([3, 2, 3]))
print(s1.majorityElement([2, 2, 1, 1, 1, 2, 2]))
