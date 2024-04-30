from typing import List
import os


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)


s1 = Solution()
print(s1.longestCommonPrefix(['flow', 'flower', 'flew']))
print(s1.longestCommonPrefix(['a']))
