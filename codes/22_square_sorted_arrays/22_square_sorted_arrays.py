from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            lst.append(abs(pow(i, 2)))
        return sorted(lst)


s = Solution()

print(s.sortedSquares([-4, -1, 0, 3, 10]))
