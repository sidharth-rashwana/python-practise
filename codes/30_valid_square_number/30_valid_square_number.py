import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        number = math.sqrt(num)
        return number.is_integer()


s = Solution()
print(s.isPerfectSquare(4))
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(8))
