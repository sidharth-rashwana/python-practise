from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indexes = [
            index for index,
            value in enumerate(nums) if value == target]
        return indexes


s1 = Solution()
print(s1.targetIndices([1, 2, 5, 2, 3], 2))
