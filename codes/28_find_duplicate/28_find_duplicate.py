from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for k in nums:
            if k in d:
                return k
            else:
                d[k] = 1


s1 = Solution()
print(s1.findDuplicate([1, 2, 3, 4, 3]))
