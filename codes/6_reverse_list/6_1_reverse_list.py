from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        print(s[::-1])  # or s.reverse()


solution = Solution()
input_list = ['h', 'e', 'l', 'l', 'o']
solution.reverseString(input_list)
