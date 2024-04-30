import math


class Solution:
    def mySqrt(self, x: int) -> int:
        result = math.sqrt(abs(x))
        return int(result)


m1 = Solution()
print(m1.mySqrt(4))
print(m1.mySqrt(2))
